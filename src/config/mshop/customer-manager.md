
# address
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/address/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusad."id"
 	FROM "mshop_customer_address" AS mcusad
 	:joins
 	WHERE :cond
 	ORDER BY mcusad."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/customer/manager/address/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the customer
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

* mshop/customer/manager/address/insert/ansi
* mshop/customer/manager/address/update/ansi
* mshop/customer/manager/address/newid/ansi
* mshop/customer/manager/address/delete/ansi
* mshop/customer/manager/address/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/address/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusad."id"
 	FROM "mshop_customer_address" AS mcusad
 	:joins
 	WHERE :cond
 	ORDER BY mcusad."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusad."id"
 	FROM "mshop_customer_address" AS mcusad
 	:joins
 	WHERE :cond
 	ORDER BY mcusad."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/customer/manager/address/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the customer address manager

```
mshop/customer/manager/address/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the customer address manager.

```
 mshop/customer/manager/address/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the customer address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/address/decorators/global
* mshop/customer/manager/address/decorators/local

## decorators/global

Adds a list of globally available decorators only to the customer address manager

```
mshop/customer/manager/address/decorators/global = Array
(
)
```

* Default: Array
* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer address manager.

```
 mshop/customer/manager/address/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the customer
address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/address/decorators/excludes
* mshop/customer/manager/address/decorators/local

## decorators/local

Adds a list of local decorators only to the customer address manager

```
mshop/customer/manager/address/decorators/local = Array
(
)
```

* Default: Array
* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Customer\Manager\Address\Decorator\*") around the customer
address manager.

```
 mshop/customer/manager/address/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Customer\Manager\Address\Decorator\Decorator2" only to the
customer address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/address/decorators/excludes
* mshop/customer/manager/address/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/address/delete/ansi = 
 DELETE FROM "mshop_customer_address"
 WHERE :cond AND siteid = ?
```

* Default: mshop/customer/manager/address/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the customer database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/address/insert/ansi
* mshop/customer/manager/address/update/ansi
* mshop/customer/manager/address/newid/ansi
* mshop/customer/manager/address/search/ansi
* mshop/customer/manager/address/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/address/delete/mysql = 
 DELETE FROM "mshop_customer_address"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_customer_address"
 WHERE :cond AND siteid = ?


See also:

* mshop/customer/manager/address/delete/ansi

## insert/ansi

Inserts a new customer address record into the database table

```
mshop/customer/manager/address/insert/ansi = 
 INSERT INTO "mshop_customer_address" ( :names
 	"parentid", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude", "pos",
 	"birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/customer/manager/address/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/address/update/ansi
* mshop/customer/manager/address/newid/ansi
* mshop/customer/manager/address/delete/ansi
* mshop/customer/manager/address/search/ansi
* mshop/customer/manager/address/count/ansi

## insert/mysql

Inserts a new customer address record into the database table

```
mshop/customer/manager/address/insert/mysql = 
 INSERT INTO "mshop_customer_address" ( :names
 	"parentid", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude", "pos",
 	"birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_customer_address" ( :names
 	"parentid", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude", "pos",
 	"birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/customer/manager/address/insert/ansi

## name

Class name of the used customer address manager implementation

```
mshop/customer/manager/address/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default customer address manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Customer\Manager\Address\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Customer\Manager\Address\Myaddress
```

then you have to set the this configuration option:

```
 mshop/customer/manager/address/name = Myaddress
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
mshop/customer/manager/address/newid/ansi = mshop/customer/manager/address/newid
```

* Default: mshop/customer/manager/address/newid
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
 SELECT currval('seq_mcusad_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcusad_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/customer/manager/address/insert/ansi
* mshop/customer/manager/address/update/ansi
* mshop/customer/manager/address/delete/ansi
* mshop/customer/manager/address/search/ansi
* mshop/customer/manager/address/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/address/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/customer/manager/address/newid

See also:

* mshop/customer/manager/address/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/address/search/ansi = 
 SELECT :columns
 	mcusad."id" AS "customer.address.id", mcusad."siteid" AS "customer.address.siteid",
 	mcusad."parentid" AS "customer.address.parentid", mcusad."pos" AS "customer.address.position",
 	mcusad."company" AS "customer.address.company", mcusad."vatid" AS "customer.address.vatid",
 	mcusad."salutation" AS "customer.address.salutation", mcusad."title" AS "customer.address.title",
 	mcusad."firstname" AS "customer.address.firstname", mcusad."lastname" AS "customer.address.lastname",
 	mcusad."address1" AS "customer.address.address1", mcusad."address2" AS "customer.address.address2",
 	mcusad."address3" AS "customer.address.address3", mcusad."postal" AS "customer.address.postal",
 	mcusad."city" AS "customer.address.city", mcusad."state" AS "customer.address.state",
 	mcusad."countryid" AS "customer.address.countryid", mcusad."langid" AS "customer.address.languageid",
 	mcusad."telephone" AS "customer.address.telephone", mcusad."email" AS "customer.address.email",
 	mcusad."telefax" AS "customer.address.telefax", mcusad."website" AS "customer.address.website",
 	mcusad."longitude" AS "customer.address.longitude", mcusad."latitude" AS "customer.address.latitude",
 	mcusad."mtime" AS "customer.address.mtime", mcusad."editor" AS "customer.address.editor",
 	mcusad."ctime" AS "customer.address.ctime", mcusad."birthday" AS "customer.address.birthday"
 FROM "mshop_customer_address" AS mcusad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/customer/manager/address/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the customer
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

* mshop/customer/manager/address/insert/ansi
* mshop/customer/manager/address/update/ansi
* mshop/customer/manager/address/newid/ansi
* mshop/customer/manager/address/delete/ansi
* mshop/customer/manager/address/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/address/search/mysql = 
 SELECT :columns
 	mcusad."id" AS "customer.address.id", mcusad."siteid" AS "customer.address.siteid",
 	mcusad."parentid" AS "customer.address.parentid", mcusad."pos" AS "customer.address.position",
 	mcusad."company" AS "customer.address.company", mcusad."vatid" AS "customer.address.vatid",
 	mcusad."salutation" AS "customer.address.salutation", mcusad."title" AS "customer.address.title",
 	mcusad."firstname" AS "customer.address.firstname", mcusad."lastname" AS "customer.address.lastname",
 	mcusad."address1" AS "customer.address.address1", mcusad."address2" AS "customer.address.address2",
 	mcusad."address3" AS "customer.address.address3", mcusad."postal" AS "customer.address.postal",
 	mcusad."city" AS "customer.address.city", mcusad."state" AS "customer.address.state",
 	mcusad."countryid" AS "customer.address.countryid", mcusad."langid" AS "customer.address.languageid",
 	mcusad."telephone" AS "customer.address.telephone", mcusad."email" AS "customer.address.email",
 	mcusad."telefax" AS "customer.address.telefax", mcusad."website" AS "customer.address.website",
 	mcusad."longitude" AS "customer.address.longitude", mcusad."latitude" AS "customer.address.latitude",
 	mcusad."mtime" AS "customer.address.mtime", mcusad."editor" AS "customer.address.editor",
 	mcusad."ctime" AS "customer.address.ctime", mcusad."birthday" AS "customer.address.birthday"
 FROM "mshop_customer_address" AS mcusad
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcusad."id" AS "customer.address.id", mcusad."siteid" AS "customer.address.siteid",
 	mcusad."parentid" AS "customer.address.parentid", mcusad."pos" AS "customer.address.position",
 	mcusad."company" AS "customer.address.company", mcusad."vatid" AS "customer.address.vatid",
 	mcusad."salutation" AS "customer.address.salutation", mcusad."title" AS "customer.address.title",
 	mcusad."firstname" AS "customer.address.firstname", mcusad."lastname" AS "customer.address.lastname",
 	mcusad."address1" AS "customer.address.address1", mcusad."address2" AS "customer.address.address2",
 	mcusad."address3" AS "customer.address.address3", mcusad."postal" AS "customer.address.postal",
 	mcusad."city" AS "customer.address.city", mcusad."state" AS "customer.address.state",
 	mcusad."countryid" AS "customer.address.countryid", mcusad."langid" AS "customer.address.languageid",
 	mcusad."telephone" AS "customer.address.telephone", mcusad."email" AS "customer.address.email",
 	mcusad."telefax" AS "customer.address.telefax", mcusad."website" AS "customer.address.website",
 	mcusad."longitude" AS "customer.address.longitude", mcusad."latitude" AS "customer.address.latitude",
 	mcusad."mtime" AS "customer.address.mtime", mcusad."editor" AS "customer.address.editor",
 	mcusad."ctime" AS "customer.address.ctime", mcusad."birthday" AS "customer.address.birthday"
 FROM "mshop_customer_address" AS mcusad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/customer/manager/address/search/ansi

## submanagers

List of manager names that can be instantiated by the customer address manager

```
mshop/customer/manager/address/submanagers = Array
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

Updates an existing customer address record in the database

```
mshop/customer/manager/address/update/ansi = 
 UPDATE "mshop_customer_address"
 SET :names
 	"parentid" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?,
 	"address2" = ?, "address3" = ?, "postal" = ?, "city" = ?,
 	"state" = ?, "countryid" = ?, "langid" = ?, "telephone" = ?,
 	"email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?, "siteid" = ?
 WHERE "id" = ?
```

* Default: mshop/customer/manager/address/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/address/insert/ansi
* mshop/customer/manager/address/newid/ansi
* mshop/customer/manager/address/delete/ansi
* mshop/customer/manager/address/search/ansi
* mshop/customer/manager/address/count/ansi

## update/mysql

Updates an existing customer address record in the database

```
mshop/customer/manager/address/update/mysql = 
 UPDATE "mshop_customer_address"
 SET :names
 	"parentid" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?,
 	"address2" = ?, "address3" = ?, "postal" = ?, "city" = ?,
 	"state" = ?, "countryid" = ?, "langid" = ?, "telephone" = ?,
 	"email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?, "siteid" = ?
 WHERE "id" = ?
```

* Default: 
 UPDATE "mshop_customer_address"
 SET :names
 	"parentid" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?,
 	"address2" = ?, "address3" = ?, "postal" = ?, "city" = ?,
 	"state" = ?, "countryid" = ?, "langid" = ?, "telephone" = ?,
 	"email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?, "siteid" = ?
 WHERE "id" = ?


See also:

* mshop/customer/manager/address/update/ansi

# aggregate
## ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_customer" AS mcus
 	:joins
 	WHERE :cond
 	GROUP BY mcus.id, :cols, :val
 	ORDER BY mcus.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/customer/manager/aggregate
* Type: string - SQL statement for aggregating customer items
* Since: 2021.04

Groups all records by the values in the key column and counts their
occurence. The matched records can be limited by the given criteria
from the customer database. The records must be from one of the sites
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

* mshop/customer/manager/insert/ansi
* mshop/customer/manager/update/ansi
* mshop/customer/manager/newid/ansi
* mshop/customer/manager/delete/ansi
* mshop/customer/manager/search/ansi
* mshop/customer/manager/count/ansi

## mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_customer" AS mcus
 	:joins
 	WHERE :cond
 	GROUP BY mcus.id, :cols, :val
 	ORDER BY mcus.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_customer" AS mcus
 	:joins
 	WHERE :cond
 	GROUP BY mcus.id, :cols, :val
 	ORDER BY mcus.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/customer/manager/aggregate/ansi

# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcus."id"
 	FROM "mshop_customer" AS mcus
 	:joins
 	WHERE :cond
 	GROUP BY mcus."id"
 	ORDER BY mcus."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/customer/manager/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the customer
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

* mshop/customer/manager/insert/ansi
* mshop/customer/manager/update/ansi
* mshop/customer/manager/newid/ansi
* mshop/customer/manager/delete/ansi
* mshop/customer/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcus."id"
 	FROM "mshop_customer" AS mcus
 	:joins
 	WHERE :cond
 	GROUP BY mcus."id"
 	ORDER BY mcus."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcus."id"
 	FROM "mshop_customer" AS mcus
 	:joins
 	WHERE :cond
 	GROUP BY mcus."id"
 	ORDER BY mcus."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/customer/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the customer manager

```
mshop/customer/manager/decorators/excludes = Array
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
around the customer manager.

```
 mshop/customer/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the customer manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/decorators/global
* mshop/customer/manager/decorators/local

## global

Adds a list of globally available decorators only to the customer manager

```
mshop/customer/manager/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer manager.

```
 mshop/customer/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the customer
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/decorators/excludes
* mshop/customer/manager/decorators/local

## local

Adds a list of local decorators only to the customer manager

```
mshop/customer/manager/decorators/local = Array
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
("\Aimeos\MShop\Customer\Manager\Decorator\*") around the customer manager.

```
 mshop/customer/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Customer\Manager\Decorator\Decorator2" only to the customer
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/decorators/excludes
* mshop/customer/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/delete/ansi = 
 DELETE FROM "mshop_customer"
 WHERE :cond AND "siteid" = ?
```

* Default: mshop/customer/manager/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the customer database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/insert/ansi
* mshop/customer/manager/update/ansi
* mshop/customer/manager/newid/ansi
* mshop/customer/manager/search/ansi
* mshop/customer/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/delete/mysql = 
 DELETE FROM "mshop_customer"
 WHERE :cond AND "siteid" = ?
```

* Default: 
 DELETE FROM "mshop_customer"
 WHERE :cond AND "siteid" = ?


See also:

* mshop/customer/manager/delete/ansi

# fosuser
## insert

Inserts a new customer record into the database table

```
mshop/customer/manager/fosuser/insert = 
```

* Default: 
* Type: string - SQL statement for inserting records
* Since: 2015.01

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/fosuser/update
* mshop/customer/manager/fosuser/newid
* mshop/customer/manager/fosuser/delete
* mshop/customer/manager/fosuser/search
* mshop/customer/manager/fosuser/count

## newid

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/fosuser/newid = 
```

* Default: 
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2015.01

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

* mshop/customer/manager/fosuser/insert
* mshop/customer/manager/fosuser/update
* mshop/customer/manager/fosuser/delete
* mshop/customer/manager/fosuser/search
* mshop/customer/manager/fosuser/count

## update

Updates an existing customer record in the database

```
mshop/customer/manager/fosuser/update = 
```

* Default: 
* Type: string - SQL statement for updating records
* Since: 2015.01

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/fosuser/insert
* mshop/customer/manager/fosuser/newid
* mshop/customer/manager/fosuser/delete
* mshop/customer/manager/fosuser/search
* mshop/customer/manager/fosuser/count

# group
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/group/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusgr."id"
 	FROM "mshop_customer_group" AS mcusgr
 	:joins
 	WHERE :cond
 	ORDER BY mcusgr."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/customer/manager/group/count
* Type: string - SQL statement for counting items
* Since: 2015.08

Counts all records matched by the given criteria from the customer
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

* mshop/customer/manager/group/insert/ansi
* mshop/customer/manager/group/update/ansi
* mshop/customer/manager/group/newid/ansi
* mshop/customer/manager/group/delete/ansi
* mshop/customer/manager/group/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/group/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusgr."id"
 	FROM "mshop_customer_group" AS mcusgr
 	:joins
 	WHERE :cond
 	ORDER BY mcusgr."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusgr."id"
 	FROM "mshop_customer_group" AS mcusgr
 	:joins
 	WHERE :cond
 	ORDER BY mcusgr."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/customer/manager/group/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the customer group manager

```
mshop/customer/manager/group/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/group/decorators/default" before they are wrapped
around the customer group manager.

```
 mshop/customer/manager/group/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the customer group manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/group/decorators/global
* mshop/customer/manager/group/decorators/local

## decorators/global

Adds a list of globally available decorators only to the customer group manager

```
mshop/customer/manager/group/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer manager.

```
 mshop/customer/manager/group/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the customer
group manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/group/decorators/excludes
* mshop/customer/manager/group/decorators/local

## decorators/local

Adds a list of local decorators only to the customer group manager

```
mshop/customer/manager/group/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Customer\Manager\Group\Decorator\*") around the customer
group manager.

```
 mshop/customer/manager/group/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Customer\Manager\Group\Decorator\Decorator2" only to the
customer group manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/group/decorators/excludes
* mshop/customer/manager/group/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/group/delete/ansi = 
 DELETE FROM "mshop_customer_group"
 WHERE :cond AND siteid = ?
```

* Default: mshop/customer/manager/group/delete
* Type: string - SQL statement for deleting items
* Since: 2015.08

Removes the records specified by the given IDs from the customer group
database. The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/group/insert/ansi
* mshop/customer/manager/group/update/ansi
* mshop/customer/manager/group/newid/ansi
* mshop/customer/manager/group/search/ansi
* mshop/customer/manager/group/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/group/delete/mysql = 
 DELETE FROM "mshop_customer_group"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_customer_group"
 WHERE :cond AND siteid = ?


See also:

* mshop/customer/manager/group/delete/ansi

## insert/ansi

Inserts a new customer group record into the database table

```
mshop/customer/manager/group/insert/ansi = 
 INSERT INTO "mshop_customer_group" ( :names
 	"code", "label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/customer/manager/group/insert
* Type: string - SQL statement for inserting records
* Since: 2015.08

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer group item to the statement before
they are sent to the database server. The number of question
marks must be the same as the number of columns listed in the
INSERT statement. The order of the columns must correspond to
the order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/group/update/ansi
* mshop/customer/manager/group/newid/ansi
* mshop/customer/manager/group/delete/ansi
* mshop/customer/manager/group/search/ansi
* mshop/customer/manager/group/count/ansi

## insert/mysql

Inserts a new customer group record into the database table

```
mshop/customer/manager/group/insert/mysql = 
 INSERT INTO "mshop_customer_group" ( :names
 	"code", "label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_customer_group" ( :names
 	"code", "label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )


See also:

* mshop/customer/manager/group/insert/ansi

## name

Class name of the used customer group manager implementation

```
mshop/customer/manager/group/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2015.08

Each default customer group manager can be replaced by an alternative
imlementation. To use this implementation, you have to set the last
part of the class name as configuration value so the manager factory
knows which class it has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Customer\Manager\Group\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Customer\Manager\Group\Mygroup
```

then you have to set the this configuration option:

```
 mshop/customer/manager/group/name = Mygroup
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyGroup"!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/group/newid/ansi = mshop/customer/manager/group/newid
```

* Default: mshop/customer/manager/group/newid
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

* mshop/customer/manager/group/insert/ansi
* mshop/customer/manager/group/update/ansi
* mshop/customer/manager/group/delete/ansi
* mshop/customer/manager/group/search/ansi
* mshop/customer/manager/group/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/group/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/customer/manager/group/newid

See also:

* mshop/customer/manager/group/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/group/search/ansi = 
 SELECT :columns
 	mcusgr."id" AS "customer.group.id", mcusgr."siteid" AS "customer.group.siteid",
 	mcusgr."code" AS "customer.group.code", mcusgr."label" AS "customer.group.label",
 	mcusgr."mtime" AS "customer.group.mtime", mcusgr."editor" AS "customer.group.editor",
 	mcusgr."ctime" AS "customer.group.ctime"
 FROM "mshop_customer_group" AS mcusgr
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/customer/manager/group/search
* Type: string - SQL statement for searching items
* Since: 2015.08

Fetches the records matched by the given criteria from the customer
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

* mshop/customer/manager/group/insert/ansi
* mshop/customer/manager/group/update/ansi
* mshop/customer/manager/group/newid/ansi
* mshop/customer/manager/group/delete/ansi
* mshop/customer/manager/group/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/group/search/mysql = 
 SELECT :columns
 	mcusgr."id" AS "customer.group.id", mcusgr."siteid" AS "customer.group.siteid",
 	mcusgr."code" AS "customer.group.code", mcusgr."label" AS "customer.group.label",
 	mcusgr."mtime" AS "customer.group.mtime", mcusgr."editor" AS "customer.group.editor",
 	mcusgr."ctime" AS "customer.group.ctime"
 FROM "mshop_customer_group" AS mcusgr
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcusgr."id" AS "customer.group.id", mcusgr."siteid" AS "customer.group.siteid",
 	mcusgr."code" AS "customer.group.code", mcusgr."label" AS "customer.group.label",
 	mcusgr."mtime" AS "customer.group.mtime", mcusgr."editor" AS "customer.group.editor",
 	mcusgr."ctime" AS "customer.group.ctime"
 FROM "mshop_customer_group" AS mcusgr
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/customer/manager/group/search/ansi

## submanagers

List of manager names that can be instantiated by the customer group manager

```
mshop/customer/manager/group/submanagers = Array
(
)
```

* Default: Array
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


## typo3/count

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/group/typo3/count = 
```

* Default: 
* Type: string - SQL statement for counting items
* Since: 2015.08

Counts all records matched by the given criteria from the customer
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

* mshop/customer/manager/group/typo3/search

## typo3/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/group/typo3/delete/ansi = 
```

* Default: 
* Type: string - SQL statement for deleting items
* Since: 2015.08

Removes the records specified by the given IDs from the customer group
database. The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/group/typo3/insert/ansi
* mshop/customer/manager/group/typo3/update/ansi
* mshop/customer/manager/group/typo3/newid/ansi
* mshop/customer/manager/group/typo3/search/ansi
* mshop/customer/manager/group/typo3/count/ansi

## typo3/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/group/typo3/delete/mysql = 
```

* Default: 

See also:

* mshop/customer/manager/group/typo3/delete/ansi

## typo3/insert/ansi

Inserts a new customer group record into the database table

```
mshop/customer/manager/group/typo3/insert/ansi = 
```

* Default: 
* Type: string - SQL statement for inserting records
* Since: 2015.08

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer group item to the statement before
they are sent to the database server. The number of question
marks must be the same as the number of columns listed in the
INSERT statement. The order of the columns must correspond to
the order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/group/typo3/update/ansi
* mshop/customer/manager/group/typo3/newid/ansi
* mshop/customer/manager/group/typo3/delete/ansi
* mshop/customer/manager/group/typo3/search/ansi
* mshop/customer/manager/group/typo3/count/ansi

## typo3/insert/mysql

Inserts a new customer group record into the database table

```
mshop/customer/manager/group/typo3/insert/mysql = 
```

* Default: 

See also:

* mshop/customer/manager/group/typo3/insert/ansi

## typo3/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/group/typo3/newid/ansi = 
```

* Default: 
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

* mshop/customer/manager/group/typo3/insert/ansi
* mshop/customer/manager/group/typo3/update/ansi
* mshop/customer/manager/group/typo3/delete/ansi
* mshop/customer/manager/group/typo3/search/ansi
* mshop/customer/manager/group/typo3/count/ansi

## typo3/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/group/typo3/newid/mysql = 
```

* Default: 

See also:

* mshop/customer/manager/group/typo3/newid/ansi

## typo3/pid-default

Page ID the customer records are assigned to

```
mshop/customer/manager/group/typo3/pid-default = 
```

* Default: 
* Type: int - TYPO3 page ID
* Since: 2018.10

In TYPO3, you can assign fe_group records to different sysfolders based
on their page ID. These sysfolders can be use for user authorization and
therefore, you need to assign the correct page ID to customer groups
created or modified by the Aimeos admin backend.

See also:

* mshop/customer/manager/typo3/pid-default

## typo3/search

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/group/typo3/search = 
```

* Default: 
* Type: string - SQL statement for searching items
* Since: 2015.08

Fetches the records matched by the given criteria from the customer
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

* mshop/customer/manager/group/typo3/count

## typo3/update/ansi

Updates an existing customer group record in the database

```
mshop/customer/manager/group/typo3/update/ansi = 
```

* Default: 
* Type: string - SQL statement for updating records
* Since: 2015.08

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer group item to the statement before
they are sent to the database server. The order of the columns
must correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/group/typo3/insert/ansi
* mshop/customer/manager/group/typo3/newid/ansi
* mshop/customer/manager/group/typo3/delete/ansi
* mshop/customer/manager/group/typo3/search/ansi
* mshop/customer/manager/group/typo3/count/ansi

## typo3/update/mysql

Updates an existing customer group record in the database

```
mshop/customer/manager/group/typo3/update/mysql = 
```

* Default: 

See also:

* mshop/customer/manager/group/typo3/update/ansi

## update/ansi

Updates an existing customer group record in the database

```
mshop/customer/manager/group/update/ansi = 
 UPDATE "mshop_customer_group"
 SET :names
 	"code" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/customer/manager/group/update
* Type: string - SQL statement for updating records
* Since: 2015.08

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer group item to the statement before
they are sent to the database server. The order of the columns
must correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/group/insert/ansi
* mshop/customer/manager/group/newid/ansi
* mshop/customer/manager/group/delete/ansi
* mshop/customer/manager/group/search/ansi
* mshop/customer/manager/group/count/ansi

## update/mysql

Updates an existing customer group record in the database

```
mshop/customer/manager/group/update/mysql = 
 UPDATE "mshop_customer_group"
 SET :names
 	"code" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_customer_group"
 SET :names
 	"code" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/customer/manager/group/update/ansi

# insert
## ansi

Inserts a new customer record into the database table

```
mshop/customer/manager/insert/ansi = 
 INSERT INTO "mshop_customer" ( :names
 	"label", "code", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude", "birthday",
 	"status", "vdate", "password", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )
```

* Default: mshop/customer/manager/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/update/ansi
* mshop/customer/manager/newid/ansi
* mshop/customer/manager/delete/ansi
* mshop/customer/manager/search/ansi
* mshop/customer/manager/count/ansi

## mysql

Inserts a new customer record into the database table

```
mshop/customer/manager/insert/mysql = 
 INSERT INTO "mshop_customer" ( :names
 	"label", "code", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude", "birthday",
 	"status", "vdate", "password", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )
```

* Default: 
 INSERT INTO "mshop_customer" ( :names
 	"label", "code", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude", "birthday",
 	"status", "vdate", "password", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )


See also:

* mshop/customer/manager/insert/ansi

# laravel
## /aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/laravel//aggregate/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating customer items
* Since: 2021.04

Groups all records by the values in the key column and counts their
occurence. The matched records can be limited by the given criteria
from the customer database. The records must be from one of the sites
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

* mshop/customer/manager/laravel//insert/ansi
* mshop/customer/manager/laravel//update/ansi
* mshop/customer/manager/laravel//newid/ansi
* mshop/customer/manager/laravel//delete/ansi
* mshop/customer/manager/laravel//search/ansi
* mshop/customer/manager/laravel//count/ansi

## /aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/laravel//aggregate/mysql = 
```

* Default: 

See also:

* mshop/customer/manager/laravel//aggregate/ansi

## insert

Inserts a new customer record into the database table

```
mshop/customer/manager/laravel/insert = 
```

* Default: 
* Type: string - SQL statement for inserting records
* Since: 2015.01

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/laravel/update
* mshop/customer/manager/laravel/newid
* mshop/customer/manager/laravel/delete
* mshop/customer/manager/laravel/search
* mshop/customer/manager/laravel/count

## newid

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/laravel/newid = 
```

* Default: 
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2015.01

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

* mshop/customer/manager/laravel/insert
* mshop/customer/manager/laravel/update
* mshop/customer/manager/laravel/delete
* mshop/customer/manager/laravel/search
* mshop/customer/manager/laravel/count

## update

Updates an existing customer record in the database

```
mshop/customer/manager/laravel/update = 
```

* Default: 
* Type: string - SQL statement for updating records
* Since: 2015.01

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/laravel/insert
* mshop/customer/manager/laravel/newid
* mshop/customer/manager/laravel/delete
* mshop/customer/manager/laravel/search
* mshop/customer/manager/laravel/count

# lists
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/lists/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_customer_list" AS mcusli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, mcusli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/customer/manager/lists/aggregate
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

* mshop/customer/manager/lists/insert/ansi
* mshop/customer/manager/lists/update/ansi
* mshop/customer/manager/lists/newid/ansi
* mshop/customer/manager/lists/delete/ansi
* mshop/customer/manager/lists/search/ansi
* mshop/customer/manager/lists/count/ansi

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/lists/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_customer_list" AS mcusli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, mcusli."id"
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_customer_list" AS mcusli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, mcusli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/customer/manager/lists/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/lists/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusli."id"
 	FROM "mshop_customer_list" AS mcusli
 	:joins
 	WHERE :cond
 	ORDER BY mcusli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/customer/manager/lists/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the customer
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

* mshop/customer/manager/lists/insert/ansi
* mshop/customer/manager/lists/update/ansi
* mshop/customer/manager/lists/newid/ansi
* mshop/customer/manager/lists/delete/ansi
* mshop/customer/manager/lists/search/ansi
* mshop/customer/manager/lists/aggregate/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/lists/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusli."id"
 	FROM "mshop_customer_list" AS mcusli
 	:joins
 	WHERE :cond
 	ORDER BY mcusli."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusli."id"
 	FROM "mshop_customer_list" AS mcusli
 	:joins
 	WHERE :cond
 	ORDER BY mcusli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/customer/manager/lists/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the customer list manager

```
mshop/customer/manager/lists/decorators/excludes = Array
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
around the customer list manager.

```
 mshop/customer/manager/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the customer list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/lists/decorators/global
* mshop/customer/manager/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the customer list manager

```
mshop/customer/manager/lists/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer list
manager.

```
 mshop/customer/manager/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the customer
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/lists/decorators/excludes
* mshop/customer/manager/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the customer list manager

```
mshop/customer/manager/lists/decorators/local = Array
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
("\Aimeos\MShop\Customer\Manager\Lists\Decorator\*") around the customer
list manager.

```
 mshop/customer/manager/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Customer\Manager\Lists\Decorator\Decorator2" only to the
customer list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/lists/decorators/excludes
* mshop/customer/manager/lists/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/lists/delete/ansi = 
 DELETE FROM "mshop_customer_list"
 WHERE :cond AND siteid = ?
```

* Default: mshop/customer/manager/lists/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the customer database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/lists/insert/ansi
* mshop/customer/manager/lists/update/ansi
* mshop/customer/manager/lists/newid/ansi
* mshop/customer/manager/lists/search/ansi
* mshop/customer/manager/lists/count/ansi
* mshop/customer/manager/lists/aggregate/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/lists/delete/mysql = 
 DELETE FROM "mshop_customer_list"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_customer_list"
 WHERE :cond AND siteid = ?


See also:

* mshop/customer/manager/lists/delete/ansi

## insert/ansi

Inserts a new customer list record into the database table

```
mshop/customer/manager/lists/insert/ansi = 
 INSERT INTO "mshop_customer_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/customer/manager/lists/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/lists/update/ansi
* mshop/customer/manager/lists/newid/ansi
* mshop/customer/manager/lists/delete/ansi
* mshop/customer/manager/lists/search/ansi
* mshop/customer/manager/lists/count/ansi
* mshop/customer/manager/lists/aggregate/ansi

## insert/mysql

Inserts a new customer list record into the database table

```
mshop/customer/manager/lists/insert/mysql = 
 INSERT INTO "mshop_customer_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_customer_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/customer/manager/lists/insert/ansi

## name

Class name of the used customer list manager implementation

```
mshop/customer/manager/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default customer list manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Customer\Manager\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Customer\Manager\Lists\Mylist
```

then you have to set the this configuration option:

```
 mshop/customer/manager/lists/name = Mylist
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
mshop/customer/manager/lists/newid/ansi = mshop/customer/manager/lists/newid
```

* Default: mshop/customer/manager/lists/newid
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
 SELECT currval('seq_mcusli_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcusli_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/customer/manager/lists/insert/ansi
* mshop/customer/manager/lists/update/ansi
* mshop/customer/manager/lists/delete/ansi
* mshop/customer/manager/lists/search/ansi
* mshop/customer/manager/lists/count/ansi
* mshop/customer/manager/lists/aggregate/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/lists/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/customer/manager/lists/newid

See also:

* mshop/customer/manager/lists/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/lists/search/ansi = 
 SELECT :columns
 	mcusli."id" AS "customer.lists.id", mcusli."parentid" AS "customer.lists.parentid",
 	mcusli."siteid" AS "customer.lists.siteid", mcusli."type" AS "customer.lists.type",
 	mcusli."domain" AS "customer.lists.domain", mcusli."refid" AS "customer.lists.refid",
 	mcusli."start" AS "customer.lists.datestart", mcusli."end" AS "customer.lists.dateend",
 	mcusli."config" AS "customer.lists.config", mcusli."pos" AS "customer.lists.position",
 	mcusli."status" AS "customer.lists.status", mcusli."mtime" AS "customer.lists.mtime",
 	mcusli."editor" AS "customer.lists.editor", mcusli."ctime" AS "customer.lists.ctime"
 FROM "mshop_customer_list" AS mcusli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/customer/manager/lists/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the customer
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

* mshop/customer/manager/lists/insert/ansi
* mshop/customer/manager/lists/update/ansi
* mshop/customer/manager/lists/newid/ansi
* mshop/customer/manager/lists/delete/ansi
* mshop/customer/manager/lists/count/ansi
* mshop/customer/manager/lists/aggregate/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/lists/search/mysql = 
 SELECT :columns
 	mcusli."id" AS "customer.lists.id", mcusli."parentid" AS "customer.lists.parentid",
 	mcusli."siteid" AS "customer.lists.siteid", mcusli."type" AS "customer.lists.type",
 	mcusli."domain" AS "customer.lists.domain", mcusli."refid" AS "customer.lists.refid",
 	mcusli."start" AS "customer.lists.datestart", mcusli."end" AS "customer.lists.dateend",
 	mcusli."config" AS "customer.lists.config", mcusli."pos" AS "customer.lists.position",
 	mcusli."status" AS "customer.lists.status", mcusli."mtime" AS "customer.lists.mtime",
 	mcusli."editor" AS "customer.lists.editor", mcusli."ctime" AS "customer.lists.ctime"
 FROM "mshop_customer_list" AS mcusli
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcusli."id" AS "customer.lists.id", mcusli."parentid" AS "customer.lists.parentid",
 	mcusli."siteid" AS "customer.lists.siteid", mcusli."type" AS "customer.lists.type",
 	mcusli."domain" AS "customer.lists.domain", mcusli."refid" AS "customer.lists.refid",
 	mcusli."start" AS "customer.lists.datestart", mcusli."end" AS "customer.lists.dateend",
 	mcusli."config" AS "customer.lists.config", mcusli."pos" AS "customer.lists.position",
 	mcusli."status" AS "customer.lists.status", mcusli."mtime" AS "customer.lists.mtime",
 	mcusli."editor" AS "customer.lists.editor", mcusli."ctime" AS "customer.lists.ctime"
 FROM "mshop_customer_list" AS mcusli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/customer/manager/lists/search/ansi

## submanagers

List of manager names that can be instantiated by the customer list manager

```
mshop/customer/manager/lists/submanagers = Array
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
mshop/customer/manager/lists/type/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcuslity."id"
 	FROM "mshop_customer_list_type" as mcuslity
 	:joins
 	WHERE :cond
 	ORDER BY mcuslity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS LIST
```

* Default: mshop/customer/manager/lists/type/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the customer
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

* mshop/customer/manager/lists/type/insert/ansi
* mshop/customer/manager/lists/type/update/ansi
* mshop/customer/manager/lists/type/newid/ansi
* mshop/customer/manager/lists/type/delete/ansi
* mshop/customer/manager/lists/type/search/ansi

## type/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/lists/type/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcuslity."id"
 	FROM "mshop_customer_list_type" as mcuslity
 	:joins
 	WHERE :cond
 	ORDER BY mcuslity."id"
 	LIMIT 10000 OFFSET 0
 ) AS LIST
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcuslity."id"
 	FROM "mshop_customer_list_type" as mcuslity
 	:joins
 	WHERE :cond
 	ORDER BY mcuslity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS LIST


See also:

* mshop/customer/manager/lists/type/count/ansi

## type/decorators/excludes

Excludes decorators added by the "common" option from the customer list type manager

```
mshop/customer/manager/lists/type/decorators/excludes = Array
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
around the customer list type manager.

```
 mshop/customer/manager/lists/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the customer list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/lists/type/decorators/global
* mshop/customer/manager/lists/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the customer list type manager

```
mshop/customer/manager/lists/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer list type
manager.

```
 mshop/customer/manager/lists/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the customer
list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/lists/type/decorators/excludes
* mshop/customer/manager/lists/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the customer list type manager

```
mshop/customer/manager/lists/type/decorators/local = Array
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
("\Aimeos\MShop\Customer\Manager\Lists\Type\Decorator\*") around the
customer list type manager.

```
 mshop/customer/manager/lists/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Customer\Manager\Lists\Type\Decorator\Decorator2" only to the
customer list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/lists/type/decorators/excludes
* mshop/customer/manager/lists/type/decorators/global

## type/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/lists/type/delete/ansi = 
 DELETE FROM "mshop_customer_list_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/customer/manager/lists/type/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the customer database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/lists/type/insert/ansi
* mshop/customer/manager/lists/type/update/ansi
* mshop/customer/manager/lists/type/newid/ansi
* mshop/customer/manager/lists/type/search/ansi
* mshop/customer/manager/lists/type/count/ansi

## type/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/lists/type/delete/mysql = 
 DELETE FROM "mshop_customer_list_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_customer_list_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/customer/manager/lists/type/delete/ansi

## type/insert/ansi

Inserts a new customer list type record into the database table

```
mshop/customer/manager/lists/type/insert/ansi = 
 INSERT INTO "mshop_customer_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/customer/manager/lists/type/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer list type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/lists/type/update/ansi
* mshop/customer/manager/lists/type/newid/ansi
* mshop/customer/manager/lists/type/delete/ansi
* mshop/customer/manager/lists/type/search/ansi
* mshop/customer/manager/lists/type/count/ansi

## type/insert/mysql

Inserts a new customer list type record into the database table

```
mshop/customer/manager/lists/type/insert/mysql = 
 INSERT INTO "mshop_customer_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_customer_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/customer/manager/lists/type/insert/ansi

## type/name

Class name of the used customer list type manager implementation

```
mshop/customer/manager/lists/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default customer list type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Customer\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Customer\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/customer/manager/lists/type/name = Mytype
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
mshop/customer/manager/lists/type/newid/ansi = mshop/customer/manager/lists/type/newid
```

* Default: mshop/customer/manager/lists/type/newid
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
 SELECT currval('seq_mcuslity_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcuslity_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/customer/manager/lists/type/insert/ansi
* mshop/customer/manager/lists/type/update/ansi
* mshop/customer/manager/lists/type/delete/ansi
* mshop/customer/manager/lists/type/search/ansi
* mshop/customer/manager/lists/type/count/ansi

## type/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/lists/type/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/customer/manager/lists/type/newid

See also:

* mshop/customer/manager/lists/type/newid/ansi

## type/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/lists/type/search/ansi = 
 SELECT :columns
 	mcuslity."id" AS "customer.lists.type.id", mcuslity."siteid" AS "customer.lists.type.siteid",
 	mcuslity."code" AS "customer.lists.type.code", mcuslity."domain" AS "customer.lists.type.domain",
 	mcuslity."label" AS "customer.lists.type.label", mcuslity."status" AS "customer.lists.type.status",
 	mcuslity."mtime" AS "customer.lists.type.mtime", mcuslity."editor" AS "customer.lists.type.editor",
 	mcuslity."ctime" AS "customer.lists.type.ctime", mcuslity."pos" AS "customer.lists.type.position"
 FROM "mshop_customer_list_type" AS mcuslity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/customer/manager/lists/type/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the customer
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

* mshop/customer/manager/lists/type/insert/ansi
* mshop/customer/manager/lists/type/update/ansi
* mshop/customer/manager/lists/type/newid/ansi
* mshop/customer/manager/lists/type/delete/ansi
* mshop/customer/manager/lists/type/count/ansi

## type/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/lists/type/search/mysql = 
 SELECT :columns
 	mcuslity."id" AS "customer.lists.type.id", mcuslity."siteid" AS "customer.lists.type.siteid",
 	mcuslity."code" AS "customer.lists.type.code", mcuslity."domain" AS "customer.lists.type.domain",
 	mcuslity."label" AS "customer.lists.type.label", mcuslity."status" AS "customer.lists.type.status",
 	mcuslity."mtime" AS "customer.lists.type.mtime", mcuslity."editor" AS "customer.lists.type.editor",
 	mcuslity."ctime" AS "customer.lists.type.ctime", mcuslity."pos" AS "customer.lists.type.position"
 FROM "mshop_customer_list_type" AS mcuslity
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcuslity."id" AS "customer.lists.type.id", mcuslity."siteid" AS "customer.lists.type.siteid",
 	mcuslity."code" AS "customer.lists.type.code", mcuslity."domain" AS "customer.lists.type.domain",
 	mcuslity."label" AS "customer.lists.type.label", mcuslity."status" AS "customer.lists.type.status",
 	mcuslity."mtime" AS "customer.lists.type.mtime", mcuslity."editor" AS "customer.lists.type.editor",
 	mcuslity."ctime" AS "customer.lists.type.ctime", mcuslity."pos" AS "customer.lists.type.position"
 FROM "mshop_customer_list_type" AS mcuslity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/customer/manager/lists/type/search/ansi

## type/submanagers

List of manager names that can be instantiated by the customer list type manager

```
mshop/customer/manager/lists/type/submanagers = Array
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

Updates an existing customer list type record in the database

```
mshop/customer/manager/lists/type/update/ansi = 
 UPDATE "mshop_customer_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/customer/manager/lists/type/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer list type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/lists/type/insert/ansi
* mshop/customer/manager/lists/type/newid/ansi
* mshop/customer/manager/lists/type/delete/ansi
* mshop/customer/manager/lists/type/search/ansi
* mshop/customer/manager/lists/type/count/ansi

## type/update/mysql

Updates an existing customer list type record in the database

```
mshop/customer/manager/lists/type/update/mysql = 
 UPDATE "mshop_customer_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_customer_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/customer/manager/lists/type/update/ansi

## update/ansi

Updates an existing customer list record in the database

```
mshop/customer/manager/lists/update/ansi = 
 UPDATE "mshop_customer_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/customer/manager/lists/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/lists/insert/ansi
* mshop/customer/manager/lists/newid/ansi
* mshop/customer/manager/lists/delete/ansi
* mshop/customer/manager/lists/search/ansi
* mshop/customer/manager/lists/count/ansi
* mshop/customer/manager/lists/aggregate/ansi

## update/mysql

Updates an existing customer list record in the database

```
mshop/customer/manager/lists/update/mysql = 
 UPDATE "mshop_customer_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_customer_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/customer/manager/lists/update/ansi

# name

Class name of the used customer manager implementation

```
mshop/customer/manager/name = Standard
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
 \Aimeos\MShop\Customer\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Customer\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/customer/manager/name = Mymanager
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
mshop/customer/manager/newid/ansi = mshop/customer/manager/newid
```

* Default: mshop/customer/manager/newid
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

* mshop/customer/manager/insert/ansi
* mshop/customer/manager/update/ansi
* mshop/customer/manager/delete/ansi
* mshop/customer/manager/search/ansi
* mshop/customer/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/customer/manager/newid

See also:

* mshop/customer/manager/newid/ansi

# password
## name

Last part of the name for building the password helper item

```
mshop/customer/manager/password/name = Standard
```

* Default: Standard
* Type: string - Name of the password helper implementation
* Since: 2015.01

The password helper encode given passwords and salts using the
implemented hashing method in the required format. String format and
hash algorithm needs to be the same when comparing the encoded
password to the one provided by the user after login.

See also:

* mshop/customer/manager/salt
* mshop/customer/manager/password/options

## options

List of options used by the password helper classes

```
mshop/customer/manager/password/options = Array
(
)
```

* Default: Array
* Type: string - Associative list of key/value pairs
* Since: 2015.01

Each hash method may need an arbitrary number of options specific
for the hash method. This may include the number of iterations the
method is applied or the separator between salt and password.

@sse mshop/customer/manager/salt

See also:

* mshop/customer/manager/password/name

# property
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/property/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcuspr."id"
 	FROM "mshop_customer_property" AS mcuspr
 	:joins
 	WHERE :cond
 	ORDER BY mcuspr."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/customer/manager/property/count
* Type: string - SQL statement for counting items
* Since: 2018.07

Counts all records matched by the given criteria from the customer
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

* mshop/customer/manager/property/insert/ansi
* mshop/customer/manager/property/update/ansi
* mshop/customer/manager/property/newid/ansi
* mshop/customer/manager/property/delete/ansi
* mshop/customer/manager/property/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/property/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcuspr."id"
 	FROM "mshop_customer_property" AS mcuspr
 	:joins
 	WHERE :cond
 	ORDER BY mcuspr."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcuspr."id"
 	FROM "mshop_customer_property" AS mcuspr
 	:joins
 	WHERE :cond
 	ORDER BY mcuspr."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/customer/manager/property/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the customer property manager

```
mshop/customer/manager/property/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the customer property manager.

```
 mshop/customer/manager/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the customer property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/property/decorators/global
* mshop/customer/manager/property/decorators/local

## decorators/global

Adds a list of globally available decorators only to the customer property manager

```
mshop/customer/manager/property/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer property
manager.

```
 mshop/customer/manager/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the customer
property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/property/decorators/excludes
* mshop/customer/manager/property/decorators/local

## decorators/local

Adds a list of local decorators only to the customer property manager

```
mshop/customer/manager/property/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Customer\Manager\Property\Decorator\*") around the customer
property manager.

```
 mshop/customer/manager/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Customer\Manager\Property\Decorator\Decorator2" only to the
customer property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/property/decorators/excludes
* mshop/customer/manager/property/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/property/delete/ansi = 
 DELETE FROM "mshop_customer_property"
 WHERE :cond AND siteid = ?
```

* Default: mshop/customer/manager/property/delete
* Type: string - SQL statement for deleting items
* Since: 2018.07

Removes the records specified by the given IDs from the customer database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/property/insert/ansi
* mshop/customer/manager/property/update/ansi
* mshop/customer/manager/property/newid/ansi
* mshop/customer/manager/property/search/ansi
* mshop/customer/manager/property/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/property/delete/mysql = 
 DELETE FROM "mshop_customer_property"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_customer_property"
 WHERE :cond AND siteid = ?


See also:

* mshop/customer/manager/property/delete/ansi

## insert/ansi

Inserts a new customer property record into the database table

```
mshop/customer/manager/property/insert/ansi = 
 INSERT INTO "mshop_customer_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/customer/manager/property/insert
* Type: string - SQL statement for inserting records
* Since: 2018.07

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer property item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/property/update/ansi
* mshop/customer/manager/property/newid/ansi
* mshop/customer/manager/property/delete/ansi
* mshop/customer/manager/property/search/ansi
* mshop/customer/manager/property/count/ansi

## insert/mysql

Inserts a new customer property record into the database table

```
mshop/customer/manager/property/insert/mysql = 
 INSERT INTO "mshop_customer_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_customer_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/customer/manager/property/insert/ansi

## name

Class name of the used customer property manager implementation

```
mshop/customer/manager/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.07

Each default customer property manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Customer\Manager\Property\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Customer\Manager\Property\Myproperty
```

then you have to set the this configuration option:

```
 mshop/customer/manager/property/name = Myproperty
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
mshop/customer/manager/property/newid/ansi = mshop/customer/manager/property/newid
```

* Default: mshop/customer/manager/property/newid
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2018.07

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_mcuspr_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcuspr_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/customer/manager/property/insert/ansi
* mshop/customer/manager/property/update/ansi
* mshop/customer/manager/property/delete/ansi
* mshop/customer/manager/property/search/ansi
* mshop/customer/manager/property/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/property/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/customer/manager/property/newid

See also:

* mshop/customer/manager/property/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/property/search/ansi = 
 SELECT :columns
 	mcuspr."id" AS "customer.property.id", mcuspr."parentid" AS "customer.property.parentid",
 	mcuspr."siteid" AS "customer.property.siteid", mcuspr."type" AS "customer.property.type",
 	mcuspr."langid" AS "customer.property.languageid", mcuspr."value" AS "customer.property.value",
 	mcuspr."mtime" AS "customer.property.mtime", mcuspr."editor" AS "customer.property.editor",
 	mcuspr."ctime" AS "customer.property.ctime"
 FROM "mshop_customer_property" AS mcuspr
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/customer/manager/property/search
* Type: string - SQL statement for searching items
* Since: 2018.07

Fetches the records matched by the given criteria from the customer
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

* mshop/customer/manager/property/insert/ansi
* mshop/customer/manager/property/update/ansi
* mshop/customer/manager/property/newid/ansi
* mshop/customer/manager/property/delete/ansi
* mshop/customer/manager/property/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/property/search/mysql = 
 SELECT :columns
 	mcuspr."id" AS "customer.property.id", mcuspr."parentid" AS "customer.property.parentid",
 	mcuspr."siteid" AS "customer.property.siteid", mcuspr."type" AS "customer.property.type",
 	mcuspr."langid" AS "customer.property.languageid", mcuspr."value" AS "customer.property.value",
 	mcuspr."mtime" AS "customer.property.mtime", mcuspr."editor" AS "customer.property.editor",
 	mcuspr."ctime" AS "customer.property.ctime"
 FROM "mshop_customer_property" AS mcuspr
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcuspr."id" AS "customer.property.id", mcuspr."parentid" AS "customer.property.parentid",
 	mcuspr."siteid" AS "customer.property.siteid", mcuspr."type" AS "customer.property.type",
 	mcuspr."langid" AS "customer.property.languageid", mcuspr."value" AS "customer.property.value",
 	mcuspr."mtime" AS "customer.property.mtime", mcuspr."editor" AS "customer.property.editor",
 	mcuspr."ctime" AS "customer.property.ctime"
 FROM "mshop_customer_property" AS mcuspr
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/customer/manager/property/search/ansi

## submanagers

List of manager names that can be instantiated by the customer property manager

```
mshop/customer/manager/property/submanagers = Array
(
    [0] => type
)
```

* Default: Array
* Type: array - List of sub-manager names
* Since: 2018.07

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
mshop/customer/manager/property/type/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusprty."id"
 	FROM "mshop_customer_property_type" mcusprty
 	:joins
 	WHERE :cond
 	ORDER BY mcusprty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/customer/manager/property/type/count
* Type: string - SQL statement for counting items
* Since: 2018.07

Counts all records matched by the given criteria from the customer
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

* mshop/customer/manager/property/type/insert/ansi
* mshop/customer/manager/property/type/update/ansi
* mshop/customer/manager/property/type/newid/ansi
* mshop/customer/manager/property/type/delete/ansi
* mshop/customer/manager/property/type/search/ansi

## type/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/property/type/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusprty."id"
 	FROM "mshop_customer_property_type" mcusprty
 	:joins
 	WHERE :cond
 	ORDER BY mcusprty."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcusprty."id"
 	FROM "mshop_customer_property_type" mcusprty
 	:joins
 	WHERE :cond
 	ORDER BY mcusprty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/customer/manager/property/type/count/ansi

## type/decorators/excludes

Excludes decorators added by the "common" option from the customer property type manager

```
mshop/customer/manager/property/type/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the customer property type manager.

```
 mshop/customer/manager/property/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the customer property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/property/type/decorators/global
* mshop/customer/manager/property/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the customer property type manager

```
mshop/customer/manager/property/type/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer property
type manager.

```
 mshop/customer/manager/property/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the customer
property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/property/type/decorators/excludes
* mshop/customer/manager/property/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the customer property type manager

```
mshop/customer/manager/property/type/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Customer\Manager\Property\Type\Decorator\*") around the
customer property type manager.

```
 mshop/customer/manager/property/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Customer\Manager\Property\Type\Decorator\Decorator2" only to
the customer property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/property/type/decorators/excludes
* mshop/customer/manager/property/type/decorators/global

## type/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/property/type/delete/ansi = 
 DELETE FROM "mshop_customer_property_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/customer/manager/property/type/delete
* Type: string - SQL statement for deleting items
* Since: 2018.07

Removes the records specified by the given IDs from the customer database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/property/type/insert/ansi
* mshop/customer/manager/property/type/update/ansi
* mshop/customer/manager/property/type/newid/ansi
* mshop/customer/manager/property/type/search/ansi
* mshop/customer/manager/property/type/count/ansi

## type/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/property/type/delete/mysql = 
 DELETE FROM "mshop_customer_property_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_customer_property_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/customer/manager/property/type/delete/ansi

## type/insert/ansi

Inserts a new customer property type record into the database table

```
mshop/customer/manager/property/type/insert/ansi = 
 INSERT INTO "mshop_customer_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/customer/manager/property/type/insert
* Type: string - SQL statement for inserting records
* Since: 2018.07

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/property/type/update/ansi
* mshop/customer/manager/property/type/newid/ansi
* mshop/customer/manager/property/type/delete/ansi
* mshop/customer/manager/property/type/search/ansi
* mshop/customer/manager/property/type/count/ansi

## type/insert/mysql

Inserts a new customer property type record into the database table

```
mshop/customer/manager/property/type/insert/mysql = 
 INSERT INTO "mshop_customer_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_customer_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/customer/manager/property/type/insert/ansi

## type/name

Class name of the used customer property type manager implementation

```
mshop/customer/manager/property/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.07

Each default customer property type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Customer\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Customer\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/customer/manager/property/type/name = Mytype
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
mshop/customer/manager/property/type/newid/ansi = mshop/customer/manager/property/type/newid
```

* Default: mshop/customer/manager/property/type/newid
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2018.07

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_mcusprty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcusprty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/customer/manager/property/type/insert/ansi
* mshop/customer/manager/property/type/update/ansi
* mshop/customer/manager/property/type/delete/ansi
* mshop/customer/manager/property/type/search/ansi
* mshop/customer/manager/property/type/count/ansi

## type/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/property/type/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/customer/manager/property/type/newid

See also:

* mshop/customer/manager/property/type/newid/ansi

## type/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/property/type/search/ansi = 
 SELECT :columns
 	mcusprty."id" AS "customer.property.type.id", mcusprty."siteid" AS "customer.property.type.siteid",
 	mcusprty."code" AS "customer.property.type.code", mcusprty."domain" AS "customer.property.type.domain",
 	mcusprty."label" AS "customer.property.type.label", mcusprty."status" AS "customer.property.type.status",
 	mcusprty."mtime" AS "customer.property.type.mtime", mcusprty."editor" AS "customer.property.type.editor",
 	mcusprty."ctime" AS "customer.property.type.ctime", mcusprty."pos" AS "customer.property.type.position"
 FROM "mshop_customer_property_type" mcusprty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/customer/manager/property/type/search
* Type: string - SQL statement for searching items
* Since: 2018.07

Fetches the records matched by the given criteria from the customer
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

* mshop/customer/manager/property/type/insert/ansi
* mshop/customer/manager/property/type/update/ansi
* mshop/customer/manager/property/type/newid/ansi
* mshop/customer/manager/property/type/delete/ansi
* mshop/customer/manager/property/type/count/ansi

## type/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/property/type/search/mysql = 
 SELECT :columns
 	mcusprty."id" AS "customer.property.type.id", mcusprty."siteid" AS "customer.property.type.siteid",
 	mcusprty."code" AS "customer.property.type.code", mcusprty."domain" AS "customer.property.type.domain",
 	mcusprty."label" AS "customer.property.type.label", mcusprty."status" AS "customer.property.type.status",
 	mcusprty."mtime" AS "customer.property.type.mtime", mcusprty."editor" AS "customer.property.type.editor",
 	mcusprty."ctime" AS "customer.property.type.ctime", mcusprty."pos" AS "customer.property.type.position"
 FROM "mshop_customer_property_type" mcusprty
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcusprty."id" AS "customer.property.type.id", mcusprty."siteid" AS "customer.property.type.siteid",
 	mcusprty."code" AS "customer.property.type.code", mcusprty."domain" AS "customer.property.type.domain",
 	mcusprty."label" AS "customer.property.type.label", mcusprty."status" AS "customer.property.type.status",
 	mcusprty."mtime" AS "customer.property.type.mtime", mcusprty."editor" AS "customer.property.type.editor",
 	mcusprty."ctime" AS "customer.property.type.ctime", mcusprty."pos" AS "customer.property.type.position"
 FROM "mshop_customer_property_type" mcusprty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/customer/manager/property/type/search/ansi

## type/submanagers

List of manager names that can be instantiated by the customer property type manager

```
mshop/customer/manager/property/type/submanagers = Array
(
)
```

* Default: Array
* Type: array - List of sub-manager names
* Since: 2018.07

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


## type/update/ansi

Updates an existing customer property type record in the database

```
mshop/customer/manager/property/type/update/ansi = 
 UPDATE "mshop_customer_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/customer/manager/property/type/update
* Type: string - SQL statement for updating records
* Since: 2018.07

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/property/type/insert/ansi
* mshop/customer/manager/property/type/newid/ansi
* mshop/customer/manager/property/type/delete/ansi
* mshop/customer/manager/property/type/search/ansi
* mshop/customer/manager/property/type/count/ansi

## type/update/mysql

Updates an existing customer property type record in the database

```
mshop/customer/manager/property/type/update/mysql = 
 UPDATE "mshop_customer_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_customer_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/customer/manager/property/type/update/ansi

## update/ansi

Updates an existing customer property record in the database

```
mshop/customer/manager/property/update/ansi = 
 UPDATE "mshop_customer_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/customer/manager/property/update
* Type: string - SQL statement for updating records
* Since: 2018.07

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer property item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/property/insert/ansi
* mshop/customer/manager/property/newid/ansi
* mshop/customer/manager/property/delete/ansi
* mshop/customer/manager/property/search/ansi
* mshop/customer/manager/property/count/ansi

## update/mysql

Updates an existing customer property record in the database

```
mshop/customer/manager/property/update/mysql = 
 UPDATE "mshop_customer_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_customer_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/customer/manager/property/update/ansi

# salt

Password salt for all customer passwords of the installation

```
mshop/customer/manager/salt = mshop
```

* Default: mshop
* Type: string - Installation wide password salt
* Since: 2014.03

The default password salt is used if no user-specific salt can be
stored in the database along with the user data. It's highly recommended
to set the salt to a random string of at least eight chars using
characters, digits and special characters

@sse mshop/customer/manager/password/options

See also:

* mshop/customer/manager/password/name

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/search/ansi = 
 SELECT :columns
 	mcus."id" AS "customer.id", mcus."siteid" AS "customer.siteid",
 	mcus."label" AS "customer.label", mcus."code" AS "customer.code",
 	mcus."company" AS "customer.company", mcus."vatid" AS "customer.vatid",
 	mcus."salutation" AS "customer.salutation", mcus."title" AS "customer.title",
 	mcus."firstname" AS "customer.firstname", mcus."lastname" AS "customer.lastname",
 	mcus."address1" AS "customer.address1", mcus."address2" AS "customer.address2",
 	mcus."address3" AS "customer.address3", mcus."postal" AS "customer.postal",
 	mcus."city" AS "customer.city", mcus."state" AS "customer.state",
 	mcus."countryid" AS "customer.countryid", mcus."langid" AS "customer.languageid",
 	mcus."telephone" AS "customer.telephone", mcus."email" AS "customer.email",
 	mcus."telefax" AS "customer.telefax", mcus."website" AS "customer.website",
 	mcus."longitude" AS "customer.longitude", mcus."latitude" AS "customer.latitude",
 	mcus."birthday" AS "customer.birthday", mcus."status" AS "customer.status",
 	mcus."vdate" AS "customer.dateverified", mcus."password" AS "customer.password",
 	mcus."ctime" AS "customer.ctime", mcus."mtime" AS "customer.mtime",
 	mcus."editor" AS "customer.editor"
 FROM "mshop_customer" AS mcus
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mcus."id", mcus."siteid", mcus."label", mcus."code", mcus."company", mcus."vatid",
 	mcus."salutation", mcus."title", mcus."firstname", mcus."lastname", mcus."address1",
 	mcus."address2", mcus."address3", mcus."postal", mcus."city", mcus."state",
 	mcus."countryid", mcus."langid", mcus."telephone", mcus."email", mcus."telefax",
 	mcus."website", mcus."longitude", mcus."latitude", mcus."birthday", mcus."status",
 	mcus."vdate", mcus."password", mcus."ctime", mcus."mtime", mcus."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/customer/manager/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the customer
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

* mshop/customer/manager/insert/ansi
* mshop/customer/manager/update/ansi
* mshop/customer/manager/newid/ansi
* mshop/customer/manager/delete/ansi
* mshop/customer/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/search/mysql = 
 SELECT :columns
 	mcus."id" AS "customer.id", mcus."siteid" AS "customer.siteid",
 	mcus."label" AS "customer.label", mcus."code" AS "customer.code",
 	mcus."company" AS "customer.company", mcus."vatid" AS "customer.vatid",
 	mcus."salutation" AS "customer.salutation", mcus."title" AS "customer.title",
 	mcus."firstname" AS "customer.firstname", mcus."lastname" AS "customer.lastname",
 	mcus."address1" AS "customer.address1", mcus."address2" AS "customer.address2",
 	mcus."address3" AS "customer.address3", mcus."postal" AS "customer.postal",
 	mcus."city" AS "customer.city", mcus."state" AS "customer.state",
 	mcus."countryid" AS "customer.countryid", mcus."langid" AS "customer.languageid",
 	mcus."telephone" AS "customer.telephone", mcus."email" AS "customer.email",
 	mcus."telefax" AS "customer.telefax", mcus."website" AS "customer.website",
 	mcus."longitude" AS "customer.longitude", mcus."latitude" AS "customer.latitude",
 	mcus."birthday" AS "customer.birthday", mcus."status" AS "customer.status",
 	mcus."vdate" AS "customer.dateverified", mcus."password" AS "customer.password",
 	mcus."ctime" AS "customer.ctime", mcus."mtime" AS "customer.mtime",
 	mcus."editor" AS "customer.editor"
 FROM "mshop_customer" AS mcus
 :joins
 WHERE :cond
 GROUP BY :group mcus."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcus."id" AS "customer.id", mcus."siteid" AS "customer.siteid",
 	mcus."label" AS "customer.label", mcus."code" AS "customer.code",
 	mcus."company" AS "customer.company", mcus."vatid" AS "customer.vatid",
 	mcus."salutation" AS "customer.salutation", mcus."title" AS "customer.title",
 	mcus."firstname" AS "customer.firstname", mcus."lastname" AS "customer.lastname",
 	mcus."address1" AS "customer.address1", mcus."address2" AS "customer.address2",
 	mcus."address3" AS "customer.address3", mcus."postal" AS "customer.postal",
 	mcus."city" AS "customer.city", mcus."state" AS "customer.state",
 	mcus."countryid" AS "customer.countryid", mcus."langid" AS "customer.languageid",
 	mcus."telephone" AS "customer.telephone", mcus."email" AS "customer.email",
 	mcus."telefax" AS "customer.telefax", mcus."website" AS "customer.website",
 	mcus."longitude" AS "customer.longitude", mcus."latitude" AS "customer.latitude",
 	mcus."birthday" AS "customer.birthday", mcus."status" AS "customer.status",
 	mcus."vdate" AS "customer.dateverified", mcus."password" AS "customer.password",
 	mcus."ctime" AS "customer.ctime", mcus."mtime" AS "customer.mtime",
 	mcus."editor" AS "customer.editor"
 FROM "mshop_customer" AS mcus
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mcus."id", mcus."siteid", mcus."label", mcus."code", mcus."company", mcus."vatid",
 	mcus."salutation", mcus."title", mcus."firstname", mcus."lastname", mcus."address1",
 	mcus."address2", mcus."address3", mcus."postal", mcus."city", mcus."state",
 	mcus."countryid", mcus."langid", mcus."telephone", mcus."email", mcus."telefax",
 	mcus."website", mcus."longitude", mcus."latitude", mcus."birthday", mcus."status",
 	mcus."vdate", mcus."password", mcus."ctime", mcus."mtime", mcus."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/customer/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/customer/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole customer domain if items from parent sites are inherited,
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

List of manager names that can be instantiated by the customer manager

```
mshop/customer/manager/submanagers = Array
(
    [0] => address
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


# typo3
## /aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/typo3//aggregate/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating customer items
* Since: 2021.04

Groups all records by the values in the key column and counts their
occurence. The matched records can be limited by the given criteria
from the customer database. The records must be from one of the sites
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

* mshop/customer/manager/typo3//insert/ansi
* mshop/customer/manager/typo3//update/ansi
* mshop/customer/manager/typo3//newid/ansi
* mshop/customer/manager/typo3//delete/ansi
* mshop/customer/manager/typo3//search/ansi
* mshop/customer/manager/typo3//count/ansi

## /aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/typo3//aggregate/mysql = 
```

* Default: 

See also:

* mshop/customer/manager/typo3//aggregate/ansi

## insert

Inserts a new customer record into the database table

```
mshop/customer/manager/typo3/insert = 
```

* Default: 
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/typo3/update
* mshop/customer/manager/typo3/newid
* mshop/customer/manager/typo3/delete
* mshop/customer/manager/typo3/search
* mshop/customer/manager/typo3/count

## newid

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/typo3/newid = 
```

* Default: 
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

* mshop/customer/manager/typo3/insert
* mshop/customer/manager/typo3/update
* mshop/customer/manager/typo3/delete
* mshop/customer/manager/typo3/search
* mshop/customer/manager/typo3/count

## pid-default

Page ID the customer records are assigned to

```
mshop/customer/manager/typo3/pid-default = 
```

* Default: 
* Type: int - TYPO3 page ID
* Since: 2016.10

In TYPO3, you can assign fe_user records to different sysfolders based
on their page ID and for checking user credentials at login, the configured
sysfolder is used. Thus, the page ID of the same sysfolder must be assigned
to the user records so they are allowed to log in after they are created
or modified by Aimeos.

See also:

* mshop/customer/manager/group/typo3/pid-default

## update

Updates an existing customer record in the database

```
mshop/customer/manager/typo3/update = 
```

* Default: 
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/typo3/insert
* mshop/customer/manager/typo3/newid
* mshop/customer/manager/typo3/delete
* mshop/customer/manager/typo3/search
* mshop/customer/manager/typo3/count

# update
## ansi

Updates an existing customer record in the database

```
mshop/customer/manager/update/ansi = 
 UPDATE "mshop_customer"
 SET :names
 	"label" = ?, "code" = ?, "company" = ?, "vatid" = ?,
 	"salutation" = ?, "title" = ?, "firstname" = ?, "lastname" = ?,
 	"address1" = ?, "address2" = ?, "address3" = ?, "postal" = ?,
 	"city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?,
 	"longitude" = ?, "latitude" = ?, "birthday" = ?, "status" = ?,
 	"vdate" = ?, "password" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/customer/manager/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the customer item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/customer/manager/insert/ansi
* mshop/customer/manager/newid/ansi
* mshop/customer/manager/delete/ansi
* mshop/customer/manager/search/ansi
* mshop/customer/manager/count/ansi

## mysql

Updates an existing customer record in the database

```
mshop/customer/manager/update/mysql = 
 UPDATE "mshop_customer"
 SET :names
 	"label" = ?, "code" = ?, "company" = ?, "vatid" = ?,
 	"salutation" = ?, "title" = ?, "firstname" = ?, "lastname" = ?,
 	"address1" = ?, "address2" = ?, "address3" = ?, "postal" = ?,
 	"city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?,
 	"longitude" = ?, "latitude" = ?, "birthday" = ?, "status" = ?,
 	"vdate" = ?, "password" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_customer"
 SET :names
 	"label" = ?, "code" = ?, "company" = ?, "vatid" = ?,
 	"salutation" = ?, "title" = ?, "firstname" = ?, "lastname" = ?,
 	"address1" = ?, "address2" = ?, "address3" = ?, "postal" = ?,
 	"city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?,
 	"longitude" = ?, "latitude" = ?, "birthday" = ?, "status" = ?,
 	"vdate" = ?, "password" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/customer/manager/update/ansi