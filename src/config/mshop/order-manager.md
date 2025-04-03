
# address
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/address/aggregate/ansi = 
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
```


See also:

* mshop/order/manager/address/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/address/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/address/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the order base address manager

```
mshop/order/manager/address/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/address/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/address/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/address/delete/ansi

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/address/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/address/insert/ansi

## name

Class name of the used order base address manager implementation

```
mshop/order/manager/address/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
* Since: 2015.10

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
mshop/order/manager/address/newid/mysql = 
```


See also:

* mshop/order/manager/address/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/address/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/order/manager/address/insert/ansi
* mshop/order/manager/address/update/ansi
* mshop/order/manager/address/newid/ansi
* mshop/order/manager/address/delete/ansi
* mshop/order/manager/address/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/address/search/mysql = 
```


See also:

* mshop/order/manager/address/search/ansi

## submanagers

List of manager names that can be instantiated by the order base address manager

```
mshop/order/manager/address/submanagers = 
```

* Type: array - List of sub-manager names
* Since: 2015.10

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
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/address/update/ansi

# aggregate
## ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/aggregate/ansi = 
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
```


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

# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/count/ansi

# coupon
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/coupon/aggregate/ansi = 
```

* Type: string - SQL statement for aggregating order items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/coupon/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/coupon/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/coupon/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the order base coupon manager

```
mshop/order/manager/coupon/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/coupon/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
coupon manager.

```
 mshop/order/manager/coupon/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order base
coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/coupon/decorators/excludes
* mshop/order/manager/coupon/decorators/local

## decorators/local

Adds a list of local decorators only to the order base coupon manager

```
mshop/order/manager/coupon/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Order\Manager\Address\Decorator\*") around the
order base coupon manager.

```
 mshop/order/manager/coupon/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Address\Decorator\Decorator2" only
to the order base coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/coupon/decorators/excludes
* mshop/order/manager/coupon/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/coupon/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/coupon/delete/ansi

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/coupon/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/coupon/insert/ansi

## name

Class name of the used order base coupon manager implementation

```
mshop/order/manager/coupon/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

Each default order base coupon manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Address\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Address\Mycoupon
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
or numbers. Avoid chamel case names like "MyAddress"!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/coupon/newid/ansi = 
```

* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2015.10

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
mshop/order/manager/coupon/newid/mysql = 
```


See also:

* mshop/order/manager/coupon/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/coupon/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/order/manager/coupon/insert/ansi
* mshop/order/manager/coupon/update/ansi
* mshop/order/manager/coupon/newid/ansi
* mshop/order/manager/coupon/delete/ansi
* mshop/order/manager/coupon/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/coupon/search/mysql = 
```


See also:

* mshop/order/manager/coupon/search/ansi

## submanagers

List of manager names that can be instantiated by the order base coupon manager

```
mshop/order/manager/coupon/submanagers = 
```

* Type: array - List of sub-manager names
* Since: 2015.10

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
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/coupon/update/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the order manager

```
mshop/order/manager/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/delete/ansi

# insert
## ansi

Inserts a new order record into the database table

```
mshop/order/manager/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/insert/ansi

# name

Class name of the used order manager implementation

```
mshop/order/manager/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
* Since: 2015.10

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_mrul_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mrul_id".CURRVAL FROM DUAL
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
mshop/order/manager/newid/mysql = 
```


See also:

* mshop/order/manager/newid/ansi

# product
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/aggregate/ansi = 
```

* Type: string - SQL statement for aggregating order items
* Since: 2015.10

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
```


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
```


See also:

* mshop/order/manager/product/attribute/aggregate/ansi

## attribute/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/product/attribute/count/ansi

## attribute/decorators/excludes

Excludes decorators added by the "common" option from the order base product attribute manager

```
mshop/order/manager/product/attribute/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/product/attribute/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/product/attribute/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/product/attribute/delete/ansi

## attribute/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/product/attribute/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/product/attribute/insert/ansi

## attribute/name

Class name of the used order base product attribute manager implementation

```
mshop/order/manager/product/attribute/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
* Since: 2015.10

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
mshop/order/manager/product/attribute/newid/mysql = 
```


See also:

* mshop/order/manager/product/attribute/newid/ansi

## attribute/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/order/manager/product/attribute/insert/ansi
* mshop/order/manager/product/attribute/update/ansi
* mshop/order/manager/product/attribute/newid/ansi
* mshop/order/manager/product/attribute/delete/ansi
* mshop/order/manager/product/attribute/count/ansi

## attribute/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/search/mysql = 
```


See also:

* mshop/order/manager/product/attribute/search/ansi

## attribute/submanagers

List of manager names that can be instantiated by the order base product attribute manager

```
mshop/order/manager/product/attribute/submanagers = 
```

* Type: array - List of sub-manager names
* Since: 2015.10

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
* Since: 2015.10

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
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/product/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the order base product manager

```
mshop/order/manager/product/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/product/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order base
product manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/decorators/excludes
* mshop/order/manager/product/decorators/local

## decorators/local

Adds a list of local decorators only to the order base product manager

```
mshop/order/manager/product/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/product/delete/ansi

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/product/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/product/insert/ansi

## name

Class name of the used order base product manager implementation

```
mshop/order/manager/product/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
* Since: 2015.10

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
mshop/order/manager/product/newid/mysql = 
```


See also:

* mshop/order/manager/product/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/order/manager/product/insert/ansi
* mshop/order/manager/product/update/ansi
* mshop/order/manager/product/newid/ansi
* mshop/order/manager/product/delete/ansi
* mshop/order/manager/product/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/search/mysql = 
```


See also:

* mshop/order/manager/product/search/ansi

## submanagers

List of manager names that can be instantiated by the order base product manager

```
mshop/order/manager/product/submanagers = 
```

* Type: array - List of sub-manager names
* Since: 2015.10

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
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/product/update/ansi

# resource

Name of the database connection resource to use

```
mshop/order/manager/resource = 
```

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
mshop/order/manager/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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
replaces the ":order" placeholder.

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
```


See also:

* mshop/order/manager/search/ansi

# service
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/aggregate/ansi = 
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
```


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
```


See also:

* mshop/order/manager/service/attribute/aggregate/ansi

## attribute/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/service/attribute/count/ansi

## attribute/decorators/excludes

Excludes decorators added by the "common" option from the order base service attribute manager

```
mshop/order/manager/service/attribute/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/service/attribute/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/service/attribute/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/service/attribute/delete/ansi

## attribute/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/service/attribute/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/service/attribute/insert/ansi

## attribute/name

Class name of the used order base service attribute manager implementation

```
mshop/order/manager/service/attribute/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
* Since: 2015.10

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
mshop/order/manager/service/attribute/newid/mysql = 
```


See also:

* mshop/order/manager/service/attribute/newid/ansi

## attribute/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/order/manager/service/attribute/insert/ansi
* mshop/order/manager/service/attribute/update/ansi
* mshop/order/manager/service/attribute/newid/ansi
* mshop/order/manager/service/attribute/delete/ansi
* mshop/order/manager/service/attribute/count/ansi

## attribute/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/search/mysql = 
```


See also:

* mshop/order/manager/service/attribute/search/ansi

## attribute/submanagers

List of manager names that can be instantiated by the order base service attribute manager

```
mshop/order/manager/service/attribute/submanagers = 
```

* Type: array - List of sub-manager names
* Since: 2015.10

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
* Since: 2015.10

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

## transaction/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/transaction/aggregate/ansi = 
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
```


See also:

* mshop/order/manager/service/transaction/aggregate/ansi

## transaction/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/transaction/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/service/transaction/count/ansi

## transaction/decorators/excludes

Excludes decorators added by the "common" option from the order service transaction manager

```
mshop/order/manager/service/transaction/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the order service transaction manager.

```
 mshop/order/manager/service/transaction/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order service transaction manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/transaction/decorators/global
* mshop/order/manager/service/transaction/decorators/local

## transaction/decorators/global

Adds a list of globally available decorators only to the order service transaction manager

```
mshop/order/manager/service/transaction/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order
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

Adds a list of local decorators only to the order service transaction manager

```
mshop/order/manager/service/transaction/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Order\Manager\Service\Transaction\Decorator\*")
around the order service transaction manager.

```
 mshop/order/manager/service/transaction/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Service\Transaction\Decorator\Decorator2"
only to the order service transaction manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/transaction/decorators/excludes
* mshop/order/manager/service/transaction/decorators/global

## transaction/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/transaction/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/service/transaction/delete/ansi

## transaction/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/service/transaction/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/service/transaction/insert/ansi

## transaction/name

Class name of the used order service transaction manager implementation

```
mshop/order/manager/service/transaction/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

Each default order service transaction manager can be replaced by an alternative imlementation.
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
* Since: 2015.10

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
mshop/order/manager/service/transaction/newid/mysql = 
```


See also:

* mshop/order/manager/service/transaction/newid/ansi

## transaction/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/transaction/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/order/manager/service/transaction/insert/ansi
* mshop/order/manager/service/transaction/update/ansi
* mshop/order/manager/service/transaction/newid/ansi
* mshop/order/manager/service/transaction/delete/ansi
* mshop/order/manager/service/transaction/count/ansi

## transaction/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/transaction/search/mysql = 
```


See also:

* mshop/order/manager/service/transaction/search/ansi

## transaction/submanagers

List of manager names that can be instantiated by the order service transaction manager

```
mshop/order/manager/service/transaction/submanagers = 
```

* Type: array - List of sub-manager names
* Since: 2015.10

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
* Since: 2015.10

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

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/order/manager/sitemode = 
```

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
```

* Type: string - SQL statement for aggregating order items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/status/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/status/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/status/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the order status manager

```
mshop/order/manager/status/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/status/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/order/manager/status/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/order/manager/status/delete/ansi

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/status/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/status/insert/ansi

## name

Class name of the used order status manager implementation

```
mshop/order/manager/status/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
* Since: 2015.10

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
mshop/order/manager/status/newid/mysql = 
```


See also:

* mshop/order/manager/status/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/status/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/order/manager/status/insert/ansi
* mshop/order/manager/status/update/ansi
* mshop/order/manager/status/newid/ansi
* mshop/order/manager/status/delete/ansi
* mshop/order/manager/status/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/status/search/mysql = 
```


See also:

* mshop/order/manager/status/search/ansi

## submanagers

List of manager names that can be instantiated by the order status manager

```
mshop/order/manager/status/submanagers = 
```

* Type: array - List of sub-manager names
* Since: 2015.10

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
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/status/update/ansi

# submanagers

List of manager names that can be instantiated by the order manager

```
mshop/order/manager/submanagers = 
```

* Type: array - List of sub-manager names
* Since: 2015.10

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
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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
```


See also:

* mshop/order/manager/update/ansi