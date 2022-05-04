
# address
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/supplier/manager/address/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msupad."id"
 	FROM "mshop_supplier_address" msupad
 	:joins
 	WHERE :cond
 	ORDER BY msupad."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/supplier/manager/address/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the supplier
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

* mshop/supplier/manager/address/insert/ansi
* mshop/supplier/manager/address/update/ansi
* mshop/supplier/manager/address/newid/ansi
* mshop/supplier/manager/address/delete/ansi
* mshop/supplier/manager/address/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/supplier/manager/address/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msupad."id"
 	FROM "mshop_supplier_address" msupad
 	:joins
 	WHERE :cond
 	ORDER BY msupad."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msupad."id"
 	FROM "mshop_supplier_address" msupad
 	:joins
 	WHERE :cond
 	ORDER BY msupad."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/supplier/manager/address/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the supplier address manager

```
mshop/supplier/manager/address/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the supplier address manager.

```
 mshop/supplier/manager/address/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the address of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the supplier address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/address/decorators/global
* mshop/supplier/manager/address/decorators/local

## decorators/global

Adds a list of globally available decorators only to the supplier address manager

```
mshop/supplier/manager/address/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the supplier address
manager.

```
 mshop/supplier/manager/address/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the supplier
address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/address/decorators/excludes
* mshop/supplier/manager/address/decorators/local

## decorators/local

Adds a list of local decorators only to the supplier address manager

```
mshop/supplier/manager/address/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Supplier\Manager\Address\Decorator\*") around the supplier
address manager.

```
 mshop/supplier/manager/address/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Supplier\Manager\Address\Decorator\Decorator2" only to
the supplier address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/address/decorators/excludes
* mshop/supplier/manager/address/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/supplier/manager/address/delete/ansi = 
 DELETE FROM "mshop_supplier_address"
 WHERE :cond AND siteid = ?
```

* Default: mshop/supplier/manager/address/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the supplier database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/address/insert/ansi
* mshop/supplier/manager/address/update/ansi
* mshop/supplier/manager/address/newid/ansi
* mshop/supplier/manager/address/search/ansi
* mshop/supplier/manager/address/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/supplier/manager/address/delete/mysql = 
 DELETE FROM "mshop_supplier_address"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_supplier_address"
 WHERE :cond AND siteid = ?


See also:

* mshop/supplier/manager/address/delete/ansi

## insert/ansi

Inserts a new supplier address record into the database table

```
mshop/supplier/manager/address/insert/ansi = 
 INSERT INTO "mshop_supplier_address" ( :names
 	"parentid", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/supplier/manager/address/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the supplier list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/address/update/ansi
* mshop/supplier/manager/address/newid/ansi
* mshop/supplier/manager/address/delete/ansi
* mshop/supplier/manager/address/search/ansi
* mshop/supplier/manager/address/count/ansi

## insert/mysql

Inserts a new supplier address record into the database table

```
mshop/supplier/manager/address/insert/mysql = 
 INSERT INTO "mshop_supplier_address" ( :names
 	"parentid", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_supplier_address" ( :names
 	"parentid", "company", "vatid", "salutation", "title",
 	"firstname", "lastname", "address1", "address2", "address3",
 	"postal", "city", "state", "countryid", "langid", "telephone",
 	"email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/supplier/manager/address/insert/ansi

## name

Class name of the used supplier address manager implementation

```
mshop/supplier/manager/address/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default supplier address manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Supplier\Manager\Address\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Supplier\Manager\Address\Myaddress
```

then you have to set the this configuration option:

```
 mshop/supplier/manager/address/name = Myaddress
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
mshop/supplier/manager/address/newid/ansi = mshop/supplier/manager/address/newid
```

* Default: mshop/supplier/manager/address/newid
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
 SELECT currval('seq_msupad_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_msupad_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/supplier/manager/address/insert/ansi
* mshop/supplier/manager/address/update/ansi
* mshop/supplier/manager/address/delete/ansi
* mshop/supplier/manager/address/search/ansi
* mshop/supplier/manager/address/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/supplier/manager/address/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/supplier/manager/address/newid

See also:

* mshop/supplier/manager/address/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/supplier/manager/address/search/ansi = 
 SELECT :columns
 	msupad."id" AS "supplier.address.id", msupad."siteid" AS "supplier.address.siteid",
 	msupad."parentid" AS "supplier.address.parentid", msupad."pos" AS "supplier.address.position",
 	msupad."company" AS "supplier.address.company", msupad."vatid" AS "supplier.address.vatid",
 	msupad."salutation" AS "supplier.address.salutation", msupad."title" AS "supplier.address.title",
 	msupad."firstname" AS "supplier.address.firstname", msupad."lastname" AS "supplier.address.lastname",
 	msupad."address1" AS "supplier.address.address1", msupad."address2" AS "supplier.address.address2",
 	msupad."address3" AS "supplier.address.address3", msupad."postal" AS "supplier.address.postal",
 	msupad."city" AS "supplier.address.city", msupad."state" AS "supplier.address.state",
 	msupad."countryid" AS "supplier.address.countryid", msupad."langid" AS "supplier.address.languageid",
 	msupad."telephone" AS "supplier.address.telephone", msupad."email" AS "supplier.address.email",
 	msupad."telefax" AS "supplier.address.telefax", msupad."website" AS "supplier.address.website",
 	msupad."longitude" AS "supplier.address.longitude", msupad."latitude" AS "supplier.address.latitude",
 	msupad."mtime" AS "supplier.address.mtime", msupad."ctime" AS "supplier.address.ctime",
 	msupad."editor" AS "supplier.address.editor", msupad."birthday" AS "supplier.address.birthday"
 FROM "mshop_supplier_address" msupad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/supplier/manager/address/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the supplier
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

* mshop/supplier/manager/address/insert/ansi
* mshop/supplier/manager/address/update/ansi
* mshop/supplier/manager/address/newid/ansi
* mshop/supplier/manager/address/delete/ansi
* mshop/supplier/manager/address/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/supplier/manager/address/search/mysql = 
 SELECT :columns
 	msupad."id" AS "supplier.address.id", msupad."siteid" AS "supplier.address.siteid",
 	msupad."parentid" AS "supplier.address.parentid", msupad."pos" AS "supplier.address.position",
 	msupad."company" AS "supplier.address.company", msupad."vatid" AS "supplier.address.vatid",
 	msupad."salutation" AS "supplier.address.salutation", msupad."title" AS "supplier.address.title",
 	msupad."firstname" AS "supplier.address.firstname", msupad."lastname" AS "supplier.address.lastname",
 	msupad."address1" AS "supplier.address.address1", msupad."address2" AS "supplier.address.address2",
 	msupad."address3" AS "supplier.address.address3", msupad."postal" AS "supplier.address.postal",
 	msupad."city" AS "supplier.address.city", msupad."state" AS "supplier.address.state",
 	msupad."countryid" AS "supplier.address.countryid", msupad."langid" AS "supplier.address.languageid",
 	msupad."telephone" AS "supplier.address.telephone", msupad."email" AS "supplier.address.email",
 	msupad."telefax" AS "supplier.address.telefax", msupad."website" AS "supplier.address.website",
 	msupad."longitude" AS "supplier.address.longitude", msupad."latitude" AS "supplier.address.latitude",
 	msupad."mtime" AS "supplier.address.mtime", msupad."ctime" AS "supplier.address.ctime",
 	msupad."editor" AS "supplier.address.editor", msupad."birthday" AS "supplier.address.birthday"
 FROM "mshop_supplier_address" msupad
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	msupad."id" AS "supplier.address.id", msupad."siteid" AS "supplier.address.siteid",
 	msupad."parentid" AS "supplier.address.parentid", msupad."pos" AS "supplier.address.position",
 	msupad."company" AS "supplier.address.company", msupad."vatid" AS "supplier.address.vatid",
 	msupad."salutation" AS "supplier.address.salutation", msupad."title" AS "supplier.address.title",
 	msupad."firstname" AS "supplier.address.firstname", msupad."lastname" AS "supplier.address.lastname",
 	msupad."address1" AS "supplier.address.address1", msupad."address2" AS "supplier.address.address2",
 	msupad."address3" AS "supplier.address.address3", msupad."postal" AS "supplier.address.postal",
 	msupad."city" AS "supplier.address.city", msupad."state" AS "supplier.address.state",
 	msupad."countryid" AS "supplier.address.countryid", msupad."langid" AS "supplier.address.languageid",
 	msupad."telephone" AS "supplier.address.telephone", msupad."email" AS "supplier.address.email",
 	msupad."telefax" AS "supplier.address.telefax", msupad."website" AS "supplier.address.website",
 	msupad."longitude" AS "supplier.address.longitude", msupad."latitude" AS "supplier.address.latitude",
 	msupad."mtime" AS "supplier.address.mtime", msupad."ctime" AS "supplier.address.ctime",
 	msupad."editor" AS "supplier.address.editor", msupad."birthday" AS "supplier.address.birthday"
 FROM "mshop_supplier_address" msupad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/supplier/manager/address/search/ansi

## submanagers

List of manager names that can be instantiated by the supplier address manager

```
mshop/supplier/manager/address/submanagers = Array
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

Updates an existing supplier address record in the database

```
mshop/supplier/manager/address/update/ansi = 
 UPDATE "mshop_supplier_address"
 SET :names
 	"parentid" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?,
 	"address2" = ?, "address3" = ?, "postal" = ?, "city" = ?,
 	"state" = ?, "countryid" = ?, "langid" = ?, "telephone" = ?,
 	"email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/supplier/manager/address/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the supplier list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/address/insert/ansi
* mshop/supplier/manager/address/newid/ansi
* mshop/supplier/manager/address/delete/ansi
* mshop/supplier/manager/address/search/ansi
* mshop/supplier/manager/address/count/ansi

## update/mysql

Updates an existing supplier address record in the database

```
mshop/supplier/manager/address/update/mysql = 
 UPDATE "mshop_supplier_address"
 SET :names
 	"parentid" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?,
 	"address2" = ?, "address3" = ?, "postal" = ?, "city" = ?,
 	"state" = ?, "countryid" = ?, "langid" = ?, "telephone" = ?,
 	"email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_supplier_address"
 SET :names
 	"parentid" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?,
 	"address2" = ?, "address3" = ?, "postal" = ?, "city" = ?,
 	"state" = ?, "countryid" = ?, "langid" = ?, "telephone" = ?,
 	"email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/supplier/manager/address/update/ansi

# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/supplier/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msup."id"
 	FROM "mshop_supplier" msup
 	:joins
 	WHERE :cond
 	GROUP BY msup."id"
 	ORDER BY msup."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/supplier/manager/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the supplier
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

* mshop/supplier/manager/insert/ansi
* mshop/supplier/manager/update/ansi
* mshop/supplier/manager/newid/ansi
* mshop/supplier/manager/delete/ansi
* mshop/supplier/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/supplier/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msup."id"
 	FROM "mshop_supplier" msup
 	:joins
 	WHERE :cond
 	GROUP BY msup."id"
 	ORDER BY msup."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msup."id"
 	FROM "mshop_supplier" msup
 	:joins
 	WHERE :cond
 	GROUP BY msup."id"
 	ORDER BY msup."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/supplier/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the supplier manager

```
mshop/supplier/manager/decorators/excludes = Array
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
around the supplier manager.

```
 mshop/supplier/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the supplier manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/decorators/global
* mshop/supplier/manager/decorators/local

## global

Adds a list of globally available decorators only to the supplier manager

```
mshop/supplier/manager/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the supplier manager.

```
 mshop/supplier/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the supplier
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/decorators/excludes
* mshop/supplier/manager/decorators/local

## local

Adds a list of local decorators only to the supplier manager

```
mshop/supplier/manager/decorators/local = Array
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
("\Aimeos\MShop\Supplier\Manager\Decorator\*") around the supplier manager.

```
 mshop/supplier/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Supplier\Manager\Decorator\Decorator2" only to the supplier
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/decorators/excludes
* mshop/supplier/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/supplier/manager/delete/ansi = 
 DELETE FROM "mshop_supplier"
 WHERE :cond AND siteid = ?
```

* Default: mshop/supplier/manager/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the supplier database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/insert/ansi
* mshop/supplier/manager/update/ansi
* mshop/supplier/manager/newid/ansi
* mshop/supplier/manager/search/ansi
* mshop/supplier/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/supplier/manager/delete/mysql = 
 DELETE FROM "mshop_supplier"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_supplier"
 WHERE :cond AND siteid = ?


See also:

* mshop/supplier/manager/delete/ansi

# insert
## ansi

Inserts a new supplier record into the database table

```
mshop/supplier/manager/insert/ansi = 
 INSERT INTO "mshop_supplier" ( :names
 	"code", "label", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/supplier/manager/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the supplier item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/update/ansi
* mshop/supplier/manager/newid/ansi
* mshop/supplier/manager/delete/ansi
* mshop/supplier/manager/search/ansi
* mshop/supplier/manager/count/ansi

## mysql

Inserts a new supplier record into the database table

```
mshop/supplier/manager/insert/mysql = 
 INSERT INTO "mshop_supplier" ( :names
 	"code", "label", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_supplier" ( :names
 	"code", "label", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/supplier/manager/insert/ansi

# lists
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/supplier/manager/lists/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_supplier_list" msupli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, msupli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/supplier/manager/lists/aggregate
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

* mshop/supplier/manager/lists/insert/ansi
* mshop/supplier/manager/lists/update/ansi
* mshop/supplier/manager/lists/newid/ansi
* mshop/supplier/manager/lists/delete/ansi
* mshop/supplier/manager/lists/search/ansi
* mshop/supplier/manager/lists/count/ansi

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/supplier/manager/lists/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_supplier_list" msupli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, msupli."id"
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_supplier_list" msupli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, msupli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/supplier/manager/lists/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/supplier/manager/lists/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msupli."id"
 	FROM "mshop_supplier_list" msupli
 	:joins
 	WHERE :cond
 	ORDER BY msupli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/supplier/manager/lists/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the supplier
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

* mshop/supplier/manager/lists/insert/ansi
* mshop/supplier/manager/lists/update/ansi
* mshop/supplier/manager/lists/newid/ansi
* mshop/supplier/manager/lists/delete/ansi
* mshop/supplier/manager/lists/search/ansi
* mshop/supplier/manager/lists/aggregate/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/supplier/manager/lists/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msupli."id"
 	FROM "mshop_supplier_list" msupli
 	:joins
 	WHERE :cond
 	ORDER BY msupli."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msupli."id"
 	FROM "mshop_supplier_list" msupli
 	:joins
 	WHERE :cond
 	ORDER BY msupli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/supplier/manager/lists/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the supplier list manager

```
mshop/supplier/manager/lists/decorators/excludes = Array
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
around the supplier list manager.

```
 mshop/supplier/manager/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the supplier list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/lists/decorators/global
* mshop/supplier/manager/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the supplier list manager

```
mshop/supplier/manager/lists/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the supplier list
manager.

```
 mshop/supplier/manager/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the supplier
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/lists/decorators/excludes
* mshop/supplier/manager/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the supplier list manager

```
mshop/supplier/manager/lists/decorators/local = Array
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
("\Aimeos\MShop\Supplier\Manager\Lists\Decorator\*") around the supplier
list manager.

```
 mshop/supplier/manager/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Supplier\Manager\Lists\Decorator\Decorator2" only to the
supplier list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/lists/decorators/excludes
* mshop/supplier/manager/lists/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/supplier/manager/lists/delete/ansi = 
 DELETE FROM "mshop_supplier_list"
 WHERE :cond AND siteid = ?
```

* Default: mshop/supplier/manager/lists/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the supplier database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/lists/insert/ansi
* mshop/supplier/manager/lists/update/ansi
* mshop/supplier/manager/lists/newid/ansi
* mshop/supplier/manager/lists/search/ansi
* mshop/supplier/manager/lists/count/ansi
* mshop/supplier/manager/lists/aggregate/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/supplier/manager/lists/delete/mysql = 
 DELETE FROM "mshop_supplier_list"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_supplier_list"
 WHERE :cond AND siteid = ?


See also:

* mshop/supplier/manager/lists/delete/ansi

## insert/ansi

Inserts a new supplier list record into the database table

```
mshop/supplier/manager/lists/insert/ansi = 
 INSERT INTO "mshop_supplier_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/supplier/manager/lists/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the supplier list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/lists/update/ansi
* mshop/supplier/manager/lists/newid/ansi
* mshop/supplier/manager/lists/delete/ansi
* mshop/supplier/manager/lists/search/ansi
* mshop/supplier/manager/lists/count/ansi
* mshop/supplier/manager/lists/aggregate/ansi

## insert/mysql

Inserts a new supplier list record into the database table

```
mshop/supplier/manager/lists/insert/mysql = 
 INSERT INTO "mshop_supplier_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_supplier_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/supplier/manager/lists/insert/ansi

## name

Class name of the used supplier list manager implementation

```
mshop/supplier/manager/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default supplier list manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Supplier\Manager\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Supplier\Manager\Lists\Mylist
```

then you have to set the this configuration option:

```
 mshop/supplier/manager/lists/name = Mylist
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
mshop/supplier/manager/lists/newid/ansi = mshop/supplier/manager/lists/newid
```

* Default: mshop/supplier/manager/lists/newid
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
 SELECT currval('seq_msupli_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_msupli_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/supplier/manager/lists/insert/ansi
* mshop/supplier/manager/lists/update/ansi
* mshop/supplier/manager/lists/delete/ansi
* mshop/supplier/manager/lists/search/ansi
* mshop/supplier/manager/lists/count/ansi
* mshop/supplier/manager/lists/aggregate/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/supplier/manager/lists/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/supplier/manager/lists/newid

See also:

* mshop/supplier/manager/lists/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/supplier/manager/lists/search/ansi = 
 SELECT :columns
 	msupli."id" AS "supplier.lists.id", msupli."parentid" AS "supplier.lists.parentid",
 	msupli."siteid" AS "supplier.lists.siteid", msupli."type" AS "supplier.lists.type",
 	msupli."domain" AS "supplier.lists.domain", msupli."refid" AS "supplier.lists.refid",
 	msupli."start" AS "supplier.lists.datestart", msupli."end" AS "supplier.lists.dateend",
 	msupli."config" AS "supplier.lists.config", msupli."pos" AS "supplier.lists.position",
 	msupli."status" AS "supplier.lists.status", msupli."mtime" AS "supplier.lists.mtime",
 	msupli."editor" AS "supplier.lists.editor", msupli."ctime" AS "supplier.lists.ctime"
 FROM "mshop_supplier_list" msupli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/supplier/manager/lists/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the supplier
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

* mshop/supplier/manager/lists/insert/ansi
* mshop/supplier/manager/lists/update/ansi
* mshop/supplier/manager/lists/newid/ansi
* mshop/supplier/manager/lists/delete/ansi
* mshop/supplier/manager/lists/count/ansi
* mshop/supplier/manager/lists/aggregate/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/supplier/manager/lists/search/mysql = 
 SELECT :columns
 	msupli."id" AS "supplier.lists.id", msupli."parentid" AS "supplier.lists.parentid",
 	msupli."siteid" AS "supplier.lists.siteid", msupli."type" AS "supplier.lists.type",
 	msupli."domain" AS "supplier.lists.domain", msupli."refid" AS "supplier.lists.refid",
 	msupli."start" AS "supplier.lists.datestart", msupli."end" AS "supplier.lists.dateend",
 	msupli."config" AS "supplier.lists.config", msupli."pos" AS "supplier.lists.position",
 	msupli."status" AS "supplier.lists.status", msupli."mtime" AS "supplier.lists.mtime",
 	msupli."editor" AS "supplier.lists.editor", msupli."ctime" AS "supplier.lists.ctime"
 FROM "mshop_supplier_list" msupli
 USE INDEX (unq_mssupli_pid_dm_sid_ty_rid, idx_mssupli_pid_dm_sid_pos_rid, idx_mssupli_rid_dom_sid_ty, idx_mssupli_key_sid)
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	msupli."id" AS "supplier.lists.id", msupli."parentid" AS "supplier.lists.parentid",
 	msupli."siteid" AS "supplier.lists.siteid", msupli."type" AS "supplier.lists.type",
 	msupli."domain" AS "supplier.lists.domain", msupli."refid" AS "supplier.lists.refid",
 	msupli."start" AS "supplier.lists.datestart", msupli."end" AS "supplier.lists.dateend",
 	msupli."config" AS "supplier.lists.config", msupli."pos" AS "supplier.lists.position",
 	msupli."status" AS "supplier.lists.status", msupli."mtime" AS "supplier.lists.mtime",
 	msupli."editor" AS "supplier.lists.editor", msupli."ctime" AS "supplier.lists.ctime"
 FROM "mshop_supplier_list" msupli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/supplier/manager/lists/search/ansi

## submanagers

List of manager names that can be instantiated by the supplier list manager

```
mshop/supplier/manager/lists/submanagers = Array
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


## type/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/supplier/manager/lists/type/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msuplity."id"
 	FROM "mshop_supplier_list_type" msuplity
 	:joins
 	WHERE :cond
 	ORDER BY msuplity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/supplier/manager/lists/type/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the supplier
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

* mshop/supplier/manager/lists/type/insert/ansi
* mshop/supplier/manager/lists/type/update/ansi
* mshop/supplier/manager/lists/type/newid/ansi
* mshop/supplier/manager/lists/type/delete/ansi
* mshop/supplier/manager/lists/type/search/ansi

## type/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/supplier/manager/lists/type/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msuplity."id"
 	FROM "mshop_supplier_list_type" msuplity
 	:joins
 	WHERE :cond
 	ORDER BY msuplity."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msuplity."id"
 	FROM "mshop_supplier_list_type" msuplity
 	:joins
 	WHERE :cond
 	ORDER BY msuplity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/supplier/manager/lists/type/count/ansi

## type/decorators/excludes

Excludes decorators added by the "common" option from the supplier list type manager

```
mshop/supplier/manager/lists/type/decorators/excludes = Array
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
around the supplier list type manager.

```
 mshop/supplier/manager/lists/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the supplier list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/lists/type/decorators/global
* mshop/supplier/manager/lists/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the supplier list type manager

```
mshop/supplier/manager/lists/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the supplier list
type manager.

```
 mshop/supplier/manager/lists/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the supplier
list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/lists/type/decorators/excludes
* mshop/supplier/manager/lists/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the supplier list type manager

```
mshop/supplier/manager/lists/type/decorators/local = Array
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
("\Aimeos\MShop\Supplier\Manager\Lists\Type\Decorator\*") around the
supplier list type manager.

```
 mshop/supplier/manager/lists/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Supplier\Manager\Lists\Type\Decorator\Decorator2" only
to the supplier list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/supplier/manager/lists/type/decorators/excludes
* mshop/supplier/manager/lists/type/decorators/global

## type/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/supplier/manager/lists/type/delete/ansi = 
 DELETE FROM "mshop_supplier_list_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/supplier/manager/lists/type/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the supplier database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/lists/type/insert/ansi
* mshop/supplier/manager/lists/type/update/ansi
* mshop/supplier/manager/lists/type/newid/ansi
* mshop/supplier/manager/lists/type/search/ansi
* mshop/supplier/manager/lists/type/count/ansi

## type/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/supplier/manager/lists/type/delete/mysql = 
 DELETE FROM "mshop_supplier_list_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_supplier_list_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/supplier/manager/lists/type/delete/ansi

## type/insert/ansi

Inserts a new supplier list type record into the database table

```
mshop/supplier/manager/lists/type/insert/ansi = 
 INSERT INTO "mshop_supplier_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/supplier/manager/lists/type/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the supplier list type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/lists/type/update/ansi
* mshop/supplier/manager/lists/type/newid/ansi
* mshop/supplier/manager/lists/type/delete/ansi
* mshop/supplier/manager/lists/type/search/ansi
* mshop/supplier/manager/lists/type/count/ansi

## type/insert/mysql

Inserts a new supplier list type record into the database table

```
mshop/supplier/manager/lists/type/insert/mysql = 
 INSERT INTO "mshop_supplier_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_supplier_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/supplier/manager/lists/type/insert/ansi

## type/name

Class name of the used supplier list type manager implementation

```
mshop/supplier/manager/lists/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default supplier list type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Supplier\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Supplier\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/supplier/manager/lists/type/name = Mytype
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
mshop/supplier/manager/lists/type/newid/ansi = mshop/supplier/manager/lists/type/newid
```

* Default: mshop/supplier/manager/lists/type/newid
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
 SELECT currval('seq_mserlity_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mserlity_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/supplier/manager/lists/type/insert/ansi
* mshop/supplier/manager/lists/type/update/ansi
* mshop/supplier/manager/lists/type/delete/ansi
* mshop/supplier/manager/lists/type/search/ansi
* mshop/supplier/manager/lists/type/count/ansi

## type/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/supplier/manager/lists/type/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/supplier/manager/lists/type/newid

See also:

* mshop/supplier/manager/lists/type/newid/ansi

## type/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/supplier/manager/lists/type/search/ansi = 
 SELECT :columns
 	msuplity."id" AS "supplier.lists.type.id", msuplity."siteid" AS "supplier.lists.type.siteid",
 	msuplity."code" AS "supplier.lists.type.code", msuplity."domain" AS "supplier.lists.type.domain",
 	msuplity."label" AS "supplier.lists.type.label", msuplity."status" AS "supplier.lists.type.status",
 	msuplity."mtime" AS "supplier.lists.type.mtime", msuplity."editor" AS "supplier.lists.type.editor",
 	msuplity."ctime" AS "supplier.lists.type.ctime", msuplity."pos" AS "supplier.lists.type.position"
 FROM "mshop_supplier_list_type" msuplity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/supplier/manager/lists/type/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the supplier
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

* mshop/supplier/manager/lists/type/insert/ansi
* mshop/supplier/manager/lists/type/update/ansi
* mshop/supplier/manager/lists/type/newid/ansi
* mshop/supplier/manager/lists/type/delete/ansi
* mshop/supplier/manager/lists/type/count/ansi

## type/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/supplier/manager/lists/type/search/mysql = 
 SELECT :columns
 	msuplity."id" AS "supplier.lists.type.id", msuplity."siteid" AS "supplier.lists.type.siteid",
 	msuplity."code" AS "supplier.lists.type.code", msuplity."domain" AS "supplier.lists.type.domain",
 	msuplity."label" AS "supplier.lists.type.label", msuplity."status" AS "supplier.lists.type.status",
 	msuplity."mtime" AS "supplier.lists.type.mtime", msuplity."editor" AS "supplier.lists.type.editor",
 	msuplity."ctime" AS "supplier.lists.type.ctime", msuplity."pos" AS "supplier.lists.type.position"
 FROM "mshop_supplier_list_type" msuplity
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	msuplity."id" AS "supplier.lists.type.id", msuplity."siteid" AS "supplier.lists.type.siteid",
 	msuplity."code" AS "supplier.lists.type.code", msuplity."domain" AS "supplier.lists.type.domain",
 	msuplity."label" AS "supplier.lists.type.label", msuplity."status" AS "supplier.lists.type.status",
 	msuplity."mtime" AS "supplier.lists.type.mtime", msuplity."editor" AS "supplier.lists.type.editor",
 	msuplity."ctime" AS "supplier.lists.type.ctime", msuplity."pos" AS "supplier.lists.type.position"
 FROM "mshop_supplier_list_type" msuplity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/supplier/manager/lists/type/search/ansi

## type/submanagers

List of manager names that can be instantiated by the supplier list type manager

```
mshop/supplier/manager/lists/type/submanagers = Array
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


## type/update/ansi

Updates an existing supplier list type record in the database

```
mshop/supplier/manager/lists/type/update/ansi = 
 UPDATE "mshop_supplier_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/supplier/manager/lists/type/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the supplier list type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/lists/type/insert/ansi
* mshop/supplier/manager/lists/type/newid/ansi
* mshop/supplier/manager/lists/type/delete/ansi
* mshop/supplier/manager/lists/type/search/ansi
* mshop/supplier/manager/lists/type/count/ansi

## type/update/mysql

Updates an existing supplier list type record in the database

```
mshop/supplier/manager/lists/type/update/mysql = 
 UPDATE "mshop_supplier_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_supplier_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/supplier/manager/lists/type/update/ansi

## update/ansi

Updates an existing supplier list record in the database

```
mshop/supplier/manager/lists/update/ansi = 
 UPDATE "mshop_supplier_list"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/supplier/manager/lists/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the supplier list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/lists/insert/ansi
* mshop/supplier/manager/lists/newid/ansi
* mshop/supplier/manager/lists/delete/ansi
* mshop/supplier/manager/lists/search/ansi
* mshop/supplier/manager/lists/count/ansi
* mshop/supplier/manager/lists/aggregate/ansi

## update/mysql

Updates an existing supplier list record in the database

```
mshop/supplier/manager/lists/update/mysql = 
 UPDATE "mshop_supplier_list"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_supplier_list"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/supplier/manager/lists/update/ansi

# name

Class name of the used supplier manager implementation

```
mshop/supplier/manager/name = Standard
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
 \Aimeos\MShop\Supplier\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Supplier\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/supplier/manager/name = Mymanager
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
mshop/supplier/manager/newid/ansi = mshop/supplier/manager/newid
```

* Default: mshop/supplier/manager/newid
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
 SELECT currval('seq_msup_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_msup_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/supplier/manager/insert/ansi
* mshop/supplier/manager/update/ansi
* mshop/supplier/manager/delete/ansi
* mshop/supplier/manager/search/ansi
* mshop/supplier/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/supplier/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/supplier/manager/newid

See also:

* mshop/supplier/manager/newid/ansi

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/supplier/manager/search/ansi = 
 SELECT :columns
 	msup."id" AS "supplier.id", msup."siteid" AS "supplier.siteid",
 	msup."code" AS "supplier.code", msup."label" AS "supplier.label",
 	msup."status" AS "supplier.status", msup."mtime" AS "supplier.mtime",
 	msup."editor" AS "supplier.editor", msup."ctime" AS "supplier.ctime"
 FROM "mshop_supplier" msup
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	msup."id", msup."siteid", msup."code", msup."label", msup."status", msup."mtime",
 	msup."editor", msup."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/supplier/manager/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the supplier
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

* mshop/supplier/manager/insert/ansi
* mshop/supplier/manager/update/ansi
* mshop/supplier/manager/newid/ansi
* mshop/supplier/manager/delete/ansi
* mshop/supplier/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/supplier/manager/search/mysql = 
 SELECT :columns
 	msup."id" AS "supplier.id", msup."siteid" AS "supplier.siteid",
 	msup."code" AS "supplier.code", msup."label" AS "supplier.label",
 	msup."status" AS "supplier.status", msup."mtime" AS "supplier.mtime",
 	msup."editor" AS "supplier.editor", msup."ctime" AS "supplier.ctime"
 FROM "mshop_supplier" msup
 :joins
 WHERE :cond
 GROUP BY :group msup."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	msup."id" AS "supplier.id", msup."siteid" AS "supplier.siteid",
 	msup."code" AS "supplier.code", msup."label" AS "supplier.label",
 	msup."status" AS "supplier.status", msup."mtime" AS "supplier.mtime",
 	msup."editor" AS "supplier.editor", msup."ctime" AS "supplier.ctime"
 FROM "mshop_supplier" msup
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	msup."id", msup."siteid", msup."code", msup."label", msup."status", msup."mtime",
 	msup."editor", msup."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/supplier/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/supplier/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole supplier domain if items from parent sites are inherited,
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

List of manager names that can be instantiated by the supplier manager

```
mshop/supplier/manager/submanagers = Array
(
    [0] => address
)
```

* Default: Array
(
    [0] => address
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

Updates an existing supplier record in the database

```
mshop/supplier/manager/update/ansi = 
 UPDATE "mshop_supplier"
 SET :names
 	"code" = ?, "label" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/supplier/manager/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the supplier item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/supplier/manager/insert/ansi
* mshop/supplier/manager/newid/ansi
* mshop/supplier/manager/delete/ansi
* mshop/supplier/manager/search/ansi
* mshop/supplier/manager/count/ansi

## mysql

Updates an existing supplier record in the database

```
mshop/supplier/manager/update/mysql = 
 UPDATE "mshop_supplier"
 SET :names
 	"code" = ?, "label" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_supplier"
 SET :names
 	"code" = ?, "label" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/supplier/manager/update/ansi