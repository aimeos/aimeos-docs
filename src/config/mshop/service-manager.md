
# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the service
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

* mshop/service/manager/insert/ansi
* mshop/service/manager/update/ansi
* mshop/service/manager/newid/ansi
* mshop/service/manager/delete/ansi
* mshop/service/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/count/mysql = 
```


See also:

* mshop/service/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the service manager

```
mshop/service/manager/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the service manager.

```
 mshop/service/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/decorators/global
* mshop/service/manager/decorators/local

## global

Adds a list of globally available decorators only to the service manager

```
mshop/service/manager/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the service manager.

```
 mshop/service/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the service
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/decorators/excludes
* mshop/service/manager/decorators/local

## local

Adds a list of local decorators only to the service manager

```
mshop/service/manager/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Service\Manager\Decorator\*") around the service manager.

```
 mshop/service/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Service\Manager\Decorator\Decorator2" only to the service
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/decorators/excludes
* mshop/service/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the service database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/insert/ansi
* mshop/service/manager/update/ansi
* mshop/service/manager/newid/ansi
* mshop/service/manager/search/ansi
* mshop/service/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/delete/mysql = 
```


See also:

* mshop/service/manager/delete/ansi

# insert
## ansi

Inserts a new service record into the database table

```
mshop/service/manager/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/update/ansi
* mshop/service/manager/newid/ansi
* mshop/service/manager/delete/ansi
* mshop/service/manager/search/ansi
* mshop/service/manager/count/ansi

## mysql

Inserts a new service record into the database table

```
mshop/service/manager/insert/mysql = 
```


See also:

* mshop/service/manager/insert/ansi

# lists
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/lists/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

Counts all records matched by the given criteria from the service
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

* mshop/service/manager/lists/insert/ansi
* mshop/service/manager/lists/update/ansi
* mshop/service/manager/lists/newid/ansi
* mshop/service/manager/lists/delete/ansi
* mshop/service/manager/lists/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/lists/count/mysql = 
```


See also:

* mshop/service/manager/lists/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the service list manager

```
mshop/service/manager/lists/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the service list manager.

```
 mshop/service/manager/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the service list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/decorators/global
* mshop/service/manager/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the service list manager

```
mshop/service/manager/lists/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the service list
manager.

```
 mshop/service/manager/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the service
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/decorators/excludes
* mshop/service/manager/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the service list manager

```
mshop/service/manager/lists/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Service\Manager\Lists\Decorator\*") around the service
list manager.

```
 mshop/service/manager/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Service\Manager\Lists\Decorator\Decorator2" only to the
service list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/decorators/excludes
* mshop/service/manager/lists/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/lists/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

Removes the records specified by the given IDs from the service database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/insert/ansi
* mshop/service/manager/lists/update/ansi
* mshop/service/manager/lists/newid/ansi
* mshop/service/manager/lists/search/ansi
* mshop/service/manager/lists/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/lists/delete/mysql = 
```


See also:

* mshop/service/manager/lists/delete/ansi

## insert/ansi

Inserts a new service list record into the database table

```
mshop/service/manager/lists/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/update/ansi
* mshop/service/manager/lists/newid/ansi
* mshop/service/manager/lists/delete/ansi
* mshop/service/manager/lists/search/ansi
* mshop/service/manager/lists/count/ansi

## insert/mysql

Inserts a new service list record into the database table

```
mshop/service/manager/lists/insert/mysql = 
```


See also:

* mshop/service/manager/lists/insert/ansi

## name

Class name of the used service list manager implementation

```
mshop/service/manager/lists/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

Each default service list manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Service\Manager\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Service\Manager\Lists\Mylist
```

then you have to set the this configuration option:

```
 mshop/service/manager/lists/name = Mylist
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
mshop/service/manager/lists/newid/ansi = 
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
 SELECT currval('seq_mserli_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mserli_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/service/manager/lists/insert/ansi
* mshop/service/manager/lists/update/ansi
* mshop/service/manager/lists/delete/ansi
* mshop/service/manager/lists/search/ansi
* mshop/service/manager/lists/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/lists/newid/mysql = 
```


See also:

* mshop/service/manager/lists/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/lists/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

Fetches the records matched by the given criteria from the service
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

* mshop/service/manager/lists/insert/ansi
* mshop/service/manager/lists/update/ansi
* mshop/service/manager/lists/newid/ansi
* mshop/service/manager/lists/delete/ansi
* mshop/service/manager/lists/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/lists/search/mysql = 
```


See also:

* mshop/service/manager/lists/search/ansi

## submanagers

List of manager names that can be instantiated by the service list manager

```
mshop/service/manager/lists/submanagers = 
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
mshop/service/manager/lists/type/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

Counts all records matched by the given criteria from the service
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

* mshop/service/manager/lists/type/insert/ansi
* mshop/service/manager/lists/type/update/ansi
* mshop/service/manager/lists/type/newid/ansi
* mshop/service/manager/lists/type/delete/ansi
* mshop/service/manager/lists/type/search/ansi

## type/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/lists/type/count/mysql = 
```


See also:

* mshop/service/manager/lists/type/count/ansi

## type/decorators/excludes

Excludes decorators added by the "common" option from the service list type manager

```
mshop/service/manager/lists/type/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the service list type manager.

```
 mshop/service/manager/lists/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the service list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/type/decorators/global
* mshop/service/manager/lists/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the service list type manager

```
mshop/service/manager/lists/type/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the service list
type manager.

```
 mshop/service/manager/lists/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the service
list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/type/decorators/excludes
* mshop/service/manager/lists/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the service list type manager

```
mshop/service/manager/lists/type/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Service\Manager\Lists\Type\Decorator\*") around the
service list type manager.

```
 mshop/service/manager/lists/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Service\Manager\Lists\Type\Decorator\Decorator2" only
to the service list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/type/decorators/excludes
* mshop/service/manager/lists/type/decorators/global

## type/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/lists/type/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

Removes the records specified by the given IDs from the service database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/type/insert/ansi
* mshop/service/manager/lists/type/update/ansi
* mshop/service/manager/lists/type/newid/ansi
* mshop/service/manager/lists/type/search/ansi
* mshop/service/manager/lists/type/count/ansi

## type/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/lists/type/delete/mysql = 
```


See also:

* mshop/service/manager/lists/type/delete/ansi

## type/insert/ansi

Inserts a new service list type record into the database table

```
mshop/service/manager/lists/type/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service list type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/type/update/ansi
* mshop/service/manager/lists/type/newid/ansi
* mshop/service/manager/lists/type/delete/ansi
* mshop/service/manager/lists/type/search/ansi
* mshop/service/manager/lists/type/count/ansi

## type/insert/mysql

Inserts a new service list type record into the database table

```
mshop/service/manager/lists/type/insert/mysql = 
```


See also:

* mshop/service/manager/lists/type/insert/ansi

## type/name

Class name of the used service list type manager implementation

```
mshop/service/manager/lists/type/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

Each default service list type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Service\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Service\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/service/manager/lists/type/name = Mytype
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
mshop/service/manager/lists/type/newid/ansi = 
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

* mshop/service/manager/lists/type/insert/ansi
* mshop/service/manager/lists/type/update/ansi
* mshop/service/manager/lists/type/delete/ansi
* mshop/service/manager/lists/type/search/ansi
* mshop/service/manager/lists/type/count/ansi

## type/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/lists/type/newid/mysql = 
```


See also:

* mshop/service/manager/lists/type/newid/ansi

## type/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/lists/type/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

Fetches the records matched by the given criteria from the service
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

* mshop/service/manager/lists/type/insert/ansi
* mshop/service/manager/lists/type/update/ansi
* mshop/service/manager/lists/type/newid/ansi
* mshop/service/manager/lists/type/delete/ansi
* mshop/service/manager/lists/type/count/ansi

## type/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/lists/type/search/mysql = 
```


See also:

* mshop/service/manager/lists/type/search/ansi

## type/submanagers

List of manager names that can be instantiated by the service list type manager

```
mshop/service/manager/lists/type/submanagers = 
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

Updates an existing service list type record in the database

```
mshop/service/manager/lists/type/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2015.10

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service list type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/type/insert/ansi
* mshop/service/manager/lists/type/newid/ansi
* mshop/service/manager/lists/type/delete/ansi
* mshop/service/manager/lists/type/search/ansi
* mshop/service/manager/lists/type/count/ansi

## type/update/mysql

Updates an existing service list type record in the database

```
mshop/service/manager/lists/type/update/mysql = 
```


See also:

* mshop/service/manager/lists/type/update/ansi

## update/ansi

Updates an existing service list record in the database

```
mshop/service/manager/lists/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2015.10

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/insert/ansi
* mshop/service/manager/lists/newid/ansi
* mshop/service/manager/lists/delete/ansi
* mshop/service/manager/lists/search/ansi
* mshop/service/manager/lists/count/ansi

## update/mysql

Updates an existing service list record in the database

```
mshop/service/manager/lists/update/mysql = 
```


See also:

* mshop/service/manager/lists/update/ansi

# name

Class name of the used service manager implementation

```
mshop/service/manager/name = 
```

* Type: string - Last part of the class name
* Since: 2014.03

Each default manager can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Service\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Service\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/service/manager/name = Mymanager
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
mshop/service/manager/newid/ansi = 
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
 SELECT currval('seq_mser_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mser_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/service/manager/insert/ansi
* mshop/service/manager/update/ansi
* mshop/service/manager/delete/ansi
* mshop/service/manager/search/ansi
* mshop/service/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/newid/mysql = 
```


See also:

* mshop/service/manager/newid/ansi

# resource

Name of the database connection resource to use

```
mshop/service/manager/resource = 
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
mshop/service/manager/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the service
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

* mshop/service/manager/insert/ansi
* mshop/service/manager/update/ansi
* mshop/service/manager/newid/ansi
* mshop/service/manager/delete/ansi
* mshop/service/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/search/mysql = 
```


See also:

* mshop/service/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/service/manager/sitemode = 
```

* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole service domain if items from parent sites are inherited,
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

List of manager names that can be instantiated by the service manager

```
mshop/service/manager/submanagers = 
```

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
mshop/service/manager/type/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2015.10

Counts all records matched by the given criteria from the service
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

* mshop/service/manager/type/insert/ansi
* mshop/service/manager/type/update/ansi
* mshop/service/manager/type/newid/ansi
* mshop/service/manager/type/delete/ansi
* mshop/service/manager/type/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/type/count/mysql = 
```


See also:

* mshop/service/manager/type/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the service type manager

```
mshop/service/manager/type/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the service type manager.

```
 mshop/service/manager/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the service type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/type/decorators/global
* mshop/service/manager/type/decorators/local

## decorators/global

Adds a list of globally available decorators only to the service type manager

```
mshop/service/manager/type/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the service type
manager.

```
 mshop/service/manager/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the service
type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/type/decorators/excludes
* mshop/service/manager/type/decorators/local

## decorators/local

Adds a list of local decorators only to the service type manager

```
mshop/service/manager/type/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Service\Manager\Type\Decorator\*") around the service
type manager.

```
 mshop/service/manager/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Service\Manager\Type\Decorator\Decorator2" only to the
service type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/type/decorators/excludes
* mshop/service/manager/type/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/type/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2015.10

Removes the records specified by the given IDs from the service database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/type/insert/ansi
* mshop/service/manager/type/update/ansi
* mshop/service/manager/type/newid/ansi
* mshop/service/manager/type/search/ansi
* mshop/service/manager/type/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/type/delete/mysql = 
```


See also:

* mshop/service/manager/type/delete/ansi

## insert/ansi

Inserts a new service type record into the database table

```
mshop/service/manager/type/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.10

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/type/update/ansi
* mshop/service/manager/type/newid/ansi
* mshop/service/manager/type/delete/ansi
* mshop/service/manager/type/search/ansi
* mshop/service/manager/type/count/ansi

## insert/mysql

Inserts a new service type record into the database table

```
mshop/service/manager/type/insert/mysql = 
```


See also:

* mshop/service/manager/type/insert/ansi

## name

Class name of the used service type manager implementation

```
mshop/service/manager/type/name = 
```

* Type: string - Last part of the class name
* Since: 2015.10

Each default service type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Service\Manager\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Service\Manager\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/service/manager/type/name = Mytype
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
mshop/service/manager/type/newid/ansi = 
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
 SELECT currval('seq_mserty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mserty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/service/manager/type/insert/ansi
* mshop/service/manager/type/update/ansi
* mshop/service/manager/type/delete/ansi
* mshop/service/manager/type/search/ansi
* mshop/service/manager/type/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/type/newid/mysql = 
```


See also:

* mshop/service/manager/type/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/type/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2015.10

Fetches the records matched by the given criteria from the service
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

* mshop/service/manager/type/insert/ansi
* mshop/service/manager/type/update/ansi
* mshop/service/manager/type/newid/ansi
* mshop/service/manager/type/delete/ansi
* mshop/service/manager/type/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/type/search/mysql = 
```


See also:

* mshop/service/manager/type/search/ansi

## submanagers

List of manager names that can be instantiated by the service type manager

```
mshop/service/manager/type/submanagers = 
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

Updates an existing service type record in the database

```
mshop/service/manager/type/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2015.10

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/type/insert/ansi
* mshop/service/manager/type/newid/ansi
* mshop/service/manager/type/delete/ansi
* mshop/service/manager/type/search/ansi
* mshop/service/manager/type/count/ansi

## update/mysql

Updates an existing service type record in the database

```
mshop/service/manager/type/update/mysql = 
```


See also:

* mshop/service/manager/type/update/ansi

# update
## ansi

Updates an existing service record in the database

```
mshop/service/manager/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/insert/ansi
* mshop/service/manager/newid/ansi
* mshop/service/manager/delete/ansi
* mshop/service/manager/search/ansi
* mshop/service/manager/count/ansi

## mysql

Updates an existing service record in the database

```
mshop/service/manager/update/mysql = 
```


See also:

* mshop/service/manager/update/ansi