
# address
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/address/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/address/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the customer address manager

```
mshop/customer/manager/address/decorators/excludes = 
```

* Type: array - Address of decorator names
* Since: 2015.10

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
mshop/customer/manager/address/decorators/global = 
```

* Type: array - Address of decorator names
* Since: 2015.10

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
mshop/customer/manager/address/decorators/local = 
```

* Type: array - Address of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/address/delete/ansi

## insert/ansi

Inserts a new customer address record into the database table

```
mshop/customer/manager/address/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/address/insert/ansi

## name

Class name of the used customer address manager implementation

```
mshop/customer/manager/address/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
mshop/customer/manager/address/newid/ansi = 
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
mshop/customer/manager/address/newid/mysql = 
```


See also:

* mshop/customer/manager/address/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/address/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/customer/manager/address/insert/ansi
* mshop/customer/manager/address/update/ansi
* mshop/customer/manager/address/newid/ansi
* mshop/customer/manager/address/delete/ansi
* mshop/customer/manager/address/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/address/search/mysql = 
```


See also:

* mshop/customer/manager/address/search/ansi

## submanagers

List of manager names that can be instantiated by the customer address manager

```
mshop/customer/manager/address/submanagers = 
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

Updates an existing customer address record in the database

```
mshop/customer/manager/address/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/address/update/ansi

# aggregate
## ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/aggregate/ansi = 
```

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
```


See also:

* mshop/customer/manager/aggregate/ansi

# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the customer manager

```
mshop/customer/manager/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/customer/manager/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/customer/manager/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/delete/ansi

# insert
## ansi

Inserts a new customer record into the database table

```
mshop/customer/manager/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/insert/ansi

# laravel
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/laravel/aggregate/ansi = 
```

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

* mshop/customer/manager/laravel/insert/ansi
* mshop/customer/manager/laravel/update/ansi
* mshop/customer/manager/laravel/newid/ansi
* mshop/customer/manager/laravel/delete/ansi
* mshop/customer/manager/laravel/search/ansi
* mshop/customer/manager/laravel/count/ansi

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/laravel/aggregate/mysql = 
```


See also:

* mshop/customer/manager/laravel/aggregate/ansi

## insert

Inserts a new customer record into the database table

```
mshop/customer/manager/laravel/insert = 
```

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
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/lists/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/lists/count/mysql = 
```


See also:

* mshop/customer/manager/lists/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the customer list manager

```
mshop/customer/manager/lists/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/customer/manager/lists/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/customer/manager/lists/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/lists/delete/mysql = 
```


See also:

* mshop/customer/manager/lists/delete/ansi

## insert/ansi

Inserts a new customer list record into the database table

```
mshop/customer/manager/lists/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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

## insert/mysql

Inserts a new customer list record into the database table

```
mshop/customer/manager/lists/insert/mysql = 
```


See also:

* mshop/customer/manager/lists/insert/ansi

## name

Class name of the used customer list manager implementation

```
mshop/customer/manager/lists/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
mshop/customer/manager/lists/newid/ansi = 
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

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/customer/manager/lists/newid/mysql = 
```


See also:

* mshop/customer/manager/lists/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/lists/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/customer/manager/lists/insert/ansi
* mshop/customer/manager/lists/update/ansi
* mshop/customer/manager/lists/newid/ansi
* mshop/customer/manager/lists/delete/ansi
* mshop/customer/manager/lists/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/lists/search/mysql = 
```


See also:

* mshop/customer/manager/lists/search/ansi

## submanagers

List of manager names that can be instantiated by the customer list manager

```
mshop/customer/manager/lists/submanagers = 
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


## type/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/lists/type/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/lists/type/count/ansi

## type/decorators/excludes

Excludes decorators added by the "common" option from the customer list type manager

```
mshop/customer/manager/lists/type/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
mshop/customer/manager/lists/type/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer list
type manager.

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
mshop/customer/manager/lists/type/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

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
"\Aimeos\MShop\Customer\Manager\Lists\Type\Decorator\Decorator2" only
to the customer list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/lists/type/decorators/excludes
* mshop/customer/manager/lists/type/decorators/global

## type/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/lists/type/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/lists/type/delete/ansi

## type/insert/ansi

Inserts a new customer list type record into the database table

```
mshop/customer/manager/lists/type/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/lists/type/insert/ansi

## type/name

Class name of the used customer list type manager implementation

```
mshop/customer/manager/lists/type/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
mshop/customer/manager/lists/type/newid/ansi = 
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
mshop/customer/manager/lists/type/newid/mysql = 
```


See also:

* mshop/customer/manager/lists/type/newid/ansi

## type/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/lists/type/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/customer/manager/lists/type/insert/ansi
* mshop/customer/manager/lists/type/update/ansi
* mshop/customer/manager/lists/type/newid/ansi
* mshop/customer/manager/lists/type/delete/ansi
* mshop/customer/manager/lists/type/count/ansi

## type/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/lists/type/search/mysql = 
```


See also:

* mshop/customer/manager/lists/type/search/ansi

## type/submanagers

List of manager names that can be instantiated by the customer list type manager

```
mshop/customer/manager/lists/type/submanagers = 
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


## type/update/ansi

Updates an existing customer list type record in the database

```
mshop/customer/manager/lists/type/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/lists/type/update/ansi

## update/ansi

Updates an existing customer list record in the database

```
mshop/customer/manager/lists/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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

## update/mysql

Updates an existing customer list record in the database

```
mshop/customer/manager/lists/update/mysql = 
```


See also:

* mshop/customer/manager/lists/update/ansi

# name

Class name of the used customer manager implementation

```
mshop/customer/manager/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

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
mshop/customer/manager/newid/ansi = 
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
mshop/customer/manager/newid/mysql = 
```


See also:

* mshop/customer/manager/newid/ansi

# property
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/customer/manager/property/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2018.01

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
```


See also:

* mshop/customer/manager/property/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the customer property manager

```
mshop/customer/manager/property/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2018.01

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
mshop/customer/manager/property/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2018.01

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
mshop/customer/manager/property/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2018.01

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
"\Aimeos\MShop\Customer\Manager\Property\Decorator\Decorator2" only to
the customer property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/customer/manager/property/decorators/excludes
* mshop/customer/manager/property/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/customer/manager/property/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2018.01

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
```


See also:

* mshop/customer/manager/property/delete/ansi

## insert/ansi

Inserts a new customer property record into the database table

```
mshop/customer/manager/property/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2018.01

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
```


See also:

* mshop/customer/manager/property/insert/ansi

## name

Class name of the used customer property manager implementation

```
mshop/customer/manager/property/name = 
```

* Type: string - Last part of the class name
* Since: 2018.01

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
mshop/customer/manager/property/newid/ansi = 
```

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
 SELECT currval('seq_cuspr_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_cuspr_id".CURRVAL FROM DUAL
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
mshop/customer/manager/property/newid/mysql = 
```


See also:

* mshop/customer/manager/property/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/property/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2018.01

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

* mshop/customer/manager/property/insert/ansi
* mshop/customer/manager/property/update/ansi
* mshop/customer/manager/property/newid/ansi
* mshop/customer/manager/property/delete/ansi
* mshop/customer/manager/property/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/property/search/mysql = 
```


See also:

* mshop/customer/manager/property/search/ansi

## submanagers

List of manager names that can be instantiated by the customer property manager

```
mshop/customer/manager/property/submanagers = 
```

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
mshop/customer/manager/property/type/count/ansi = 
```

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
```


See also:

* mshop/customer/manager/property/type/count/ansi

## type/decorators/excludes

Excludes decorators added by the "common" option from the customer property type manager

```
mshop/customer/manager/property/type/decorators/excludes = 
```

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
mshop/customer/manager/property/type/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the customer
property type manager.

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
mshop/customer/manager/property/type/decorators/local = 
```

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
```

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
```


See also:

* mshop/customer/manager/property/type/delete/ansi

## type/insert/ansi

Inserts a new customer property type record into the database table

```
mshop/customer/manager/property/type/insert/ansi = 
```

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
```


See also:

* mshop/customer/manager/property/type/insert/ansi

## type/name

Class name of the used customer property type manager implementation

```
mshop/customer/manager/property/type/name = 
```

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
mshop/customer/manager/property/type/newid/ansi = 
```

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
mshop/customer/manager/property/type/newid/mysql = 
```


See also:

* mshop/customer/manager/property/type/newid/ansi

## type/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/property/type/search/ansi = 
```

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

* mshop/customer/manager/property/type/insert/ansi
* mshop/customer/manager/property/type/update/ansi
* mshop/customer/manager/property/type/newid/ansi
* mshop/customer/manager/property/type/delete/ansi
* mshop/customer/manager/property/type/count/ansi

## type/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/property/type/search/mysql = 
```


See also:

* mshop/customer/manager/property/type/search/ansi

## type/submanagers

List of manager names that can be instantiated by the customer property type manager

```
mshop/customer/manager/property/type/submanagers = 
```

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
```

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
```


See also:

* mshop/customer/manager/property/type/update/ansi

## update/ansi

Updates an existing customer property record in the database

```
mshop/customer/manager/property/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2018.01

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
```


See also:

* mshop/customer/manager/property/update/ansi

# resource

Name of the database connection resource to use

```
mshop/customer/manager/resource = 
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
mshop/customer/manager/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

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

* mshop/customer/manager/insert/ansi
* mshop/customer/manager/update/ansi
* mshop/customer/manager/newid/ansi
* mshop/customer/manager/delete/ansi
* mshop/customer/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/customer/manager/search/mysql = 
```


See also:

* mshop/customer/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/customer/manager/sitemode = 
```

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
mshop/customer/manager/submanagers = 
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


# typo3
## /aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/customer/manager/typo3//aggregate/ansi = 
```

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


See also:

* mshop/customer/manager/typo3//aggregate/ansi

## insert

Inserts a new customer record into the database table

```
mshop/customer/manager/typo3/insert = 
```

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

* Type: int - TYPO3 page ID
* Since: 2016.10

In TYPO3, you can assign fe_user records to different sysfolders based
on their page ID and for checking user credentials at login, the configured
sysfolder is used. Thus, the page ID of the same sysfolder must be assigned
to the user records so they are allowed to log in after they are created
or modified by Aimeos.

See also:

* mshop/group/manager/typo3/pid-default

## update

Updates an existing customer record in the database

```
mshop/customer/manager/typo3/update = 
```

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
```

* Type: string - SQL statement for updating records
* Since: 2015.10

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
```


See also:

* mshop/customer/manager/update/ansi