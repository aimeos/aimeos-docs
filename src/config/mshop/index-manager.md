
# aggregate
## ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/index/manager/aggregate/ansi = 
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

* mshop/index/manager/count/ansi
* mshop/index/manager/optimize/ansi
* mshop/index/manager/search/ansi

## mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/index/manager/aggregate/mysql = 
```


See also:

* mshop/index/manager/aggregate/ansi

# attribute
## cleanup/ansi

Deletes the index attribute records that haven't been touched

```
mshop/index/manager/attribute/cleanup/ansi = 
```

* Type: string - SQL statement for deleting the outdated attribute index records
* Since: 2014.03

During the rebuild process of the product index, the entries of all
active products will be removed and readded. Thus, no stale data for
these products will remain in the database.

All products that have been disabled since the last rebuild will be
still part of the index. The cleanup statement removes all records
that belong to products that haven't been touched during the index
rebuild because these are the disabled ones.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/attribute/count/ansi
* mshop/index/manager/attribute/delete/ansi
* mshop/index/manager/attribute/insert/ansi
* mshop/index/manager/attribute/search/ansi

## cleanup/mysql

Deletes the index attribute records that haven't been touched

```
mshop/index/manager/attribute/cleanup/mysql = 
```


See also:

* mshop/index/manager/attribute/cleanup/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/attribute/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the product index
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

* mshop/index/manager/attribute/search/ansi
* mshop/index/manager/attribute/optimize/ansi
* mshop/index/manager/attribute/aggregate/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/attribute/count/mysql = 
```


See also:

* mshop/index/manager/attribute/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the index attribute manager

```
mshop/index/manager/attribute/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the index attribute manager.

```
 mshop/index/manager/attribute/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the index attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/attribute/decorators/global
* mshop/index/manager/attribute/decorators/local

## decorators/global

Adds a list of globally available decorators only to the index attribute manager

```
mshop/index/manager/attribute/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the index attribute
manager.

```
 mshop/index/manager/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the index
attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/attribute/decorators/excludes
* mshop/index/manager/attribute/decorators/local

## decorators/local

Adds a list of local decorators only to the index attribute manager

```
mshop/index/manager/attribute/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Index\Manager\Attribute\Decorator\*") around the index
attribute manager.

```
 mshop/index/manager/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Index\Manager\Attribute\Decorator\Decorator2" only to th
index attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/attribute/decorators/excludes
* mshop/index/manager/attribute/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/attribute/delete/ansi = 
```

* Type: string - SQL statement for deleting index attribute records
* Since: 2014.03

Removes the records specified by the given IDs from the index database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/attribute/count/ansi
* mshop/index/manager/attribute/cleanup/ansi
* mshop/index/manager/attribute/insert/ansi
* mshop/index/manager/attribute/search/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/attribute/delete/mysql = 
```


See also:

* mshop/index/manager/attribute/delete/ansi

## insert/ansi

Inserts a new attribute record into the product index database

```
mshop/index/manager/attribute/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2014.03

During the product index rebuild, attributes related to a product
will be stored in the index for this product. All records
are deleted before the new ones are inserted.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the rebuild() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/attribute/cleanup/ansi
* mshop/index/manager/attribute/delete/ansi
* mshop/index/manager/attribute/search/ansi
* mshop/index/manager/attribute/count/ansi

## insert/mysql

Inserts a new attribute record into the product index database

```
mshop/index/manager/attribute/insert/mysql = 
```


See also:

* mshop/index/manager/attribute/insert/ansi

## name

Class name of the used index attribute manager implementation

```
mshop/index/manager/attribute/name = 
```

* Type: string - Last part of the class name
* Since: 2014.03

Each default index attribute manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Index\Manager\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Index\Manager\Attribute\Myattribute
```

then you have to set the this configuration option:

```
 mshop/index/manager/attribute/name = Myattribute
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAttribute"!


## optimize/ansi

Optimizes the stored attribute data for retrieving the records faster

```
mshop/index/manager/attribute/optimize/ansi = 
```

* Type: string - SQL statement for optimizing the stored attribute data
* Since: 2014.09

The SQL statement should reorganize the data in the DBMS storage to
optimize access to the records of the table or tables. Some DBMS
offer specialized statements to optimize indexes and records. This
statement doesn't return any records.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/attribute/count/ansi
* mshop/index/manager/attribute/search/ansi
* mshop/index/manager/attribute/aggregate/ansi

## optimize/mysql

Optimizes the stored attribute data for retrieving the records faster

```
mshop/index/manager/attribute/optimize/mysql = 
```


See also:

* mshop/index/manager/attribute/optimize/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/attribute/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the product index
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

* mshop/index/manager/attribute/count/ansi
* mshop/index/manager/attribute/optimize/ansi
* mshop/index/manager/attribute/aggregate/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/attribute/search/mysql = 
```


See also:

* mshop/index/manager/attribute/search/ansi

## submanagers

A list of sub-manager names used for indexing associated items to attributes

```
mshop/index/manager/attribute/submanagers = 
```

* Type: string - List of index sub-manager names
* Since: 2014.03
* Since: 2014.09

All items referenced by a product (e.g. texts, prices, media,
etc.) are added to the product index via specialized index
managers. You can add the name of new sub-managers to add more
data to the index or remove existing ones if you don't want to
index that data at all.

This option configures the sub-managers that cares about
indexing data associated to product attributes.

See also:

* mshop/index/manager/submanagers

# catalog
## cleanup/ansi

Deletes the index catalog records that haven't been touched

```
mshop/index/manager/catalog/cleanup/ansi = 
```

* Type: string - SQL statement for deleting the outdated index records
* Since: 2014.03

During the rebuild process of the product index, the entries of all
active products will be removed and readded. Thus, no stale data for
these products will remain in the database.

All products that have been disabled since the last rebuild will be
still part of the index. The cleanup statement removes all records
that belong to products that haven't been touched during the index
rebuild because these are the disabled ones.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/catalog/count/ansi
* mshop/index/manager/catalog/delete/ansi
* mshop/index/manager/catalog/insert/ansi
* mshop/index/manager/catalog/search/ansi

## cleanup/mysql

Deletes the index catalog records that haven't been touched

```
mshop/index/manager/catalog/cleanup/mysql = 
```


See also:

* mshop/index/manager/catalog/cleanup/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/catalog/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the product index
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

* mshop/index/manager/catalog/search/ansi
* mshop/index/manager/catalog/optimize/ansi
* mshop/index/manager/catalog/aggregate/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/catalog/count/mysql = 
```


See also:

* mshop/index/manager/catalog/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the index catalog manager

```
mshop/index/manager/catalog/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the index catalog manager.

```
 mshop/index/manager/catalog/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the index catalog manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/catalog/decorators/global
* mshop/index/manager/catalog/decorators/local

## decorators/global

Adds a list of globally available decorators only to the index catalog manager

```
mshop/index/manager/catalog/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the index catalog
manager.

```
 mshop/index/manager/catalog/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the index
catalog manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/catalog/decorators/excludes
* mshop/index/manager/catalog/decorators/local

## decorators/local

Adds a list of local decorators only to the index catalog manager

```
mshop/index/manager/catalog/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Index\Manager\Catalog\Decorator\*") around the index
catalog manager.

```
 mshop/index/manager/catalog/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Index\Manager\Catalog\Decorator\Decorator2" only to the
index catalog manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/catalog/decorators/excludes
* mshop/index/manager/catalog/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/catalog/delete/ansi = 
```

* Type: string - SQL statement for deleting index catalog records
* Since: 2014.03

Removes the records specified by the given IDs from the index database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/catalog/count/ansi
* mshop/index/manager/catalog/cleanup/ansi
* mshop/index/manager/catalog/insert/ansi
* mshop/index/manager/catalog/search/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/catalog/delete/mysql = 
```


See also:

* mshop/index/manager/catalog/delete/ansi

## insert/ansi

Inserts a new catalog record into the product index database

```
mshop/index/manager/catalog/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2014.03

During the product index rebuild, categories related to a
product will be stored in the index for this product. All
records are deleted before the new ones are inserted.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the rebuild() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/catalog/cleanup/ansi
* mshop/index/manager/catalog/delete/ansi
* mshop/index/manager/catalog/search/ansi
* mshop/index/manager/catalog/count/ansi

## insert/mysql

Inserts a new catalog record into the product index database

```
mshop/index/manager/catalog/insert/mysql = 
```


See also:

* mshop/index/manager/catalog/insert/ansi

## name

Class name of the used index catalog manager implementation

```
mshop/index/manager/catalog/name = 
```

* Type: string - Last part of the class name
* Since: 2014.03

Each default index catalog manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Index\Manager\Catalog\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Index\Manager\Catalog\Mycatalog
```

then you have to set the this configuration option:

```
 mshop/index/manager/catalog/name = Mycatalog
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCatalog"!


## optimize/ansi

Optimizes the stored catalog data for retrieving the records faster

```
mshop/index/manager/catalog/optimize/ansi = 
```

* Type: string - SQL statement for optimizing the stored catalog data
* Since: 2014.09

The SQL statement should reorganize the data in the DBMS storage to
optimize access to the records of the table or tables. Some DBMS
offer specialized statements to optimize indexes and records. This
statement doesn't return any records.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/catalog/count/ansi
* mshop/index/manager/catalog/search/ansi
* mshop/index/manager/catalog/aggregate/ansi

## optimize/mysql

Optimizes the stored catalog data for retrieving the records faster

```
mshop/index/manager/catalog/optimize/mysql = 
```


See also:

* mshop/index/manager/catalog/optimize/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/catalog/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the product index
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

* mshop/index/manager/catalog/count/ansi
* mshop/index/manager/catalog/optimize/ansi
* mshop/index/manager/catalog/aggregate/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/catalog/search/mysql = 
```


See also:

* mshop/index/manager/catalog/search/ansi

## submanagers

A list of sub-manager names used for indexing associated items to categories

```
mshop/index/manager/catalog/submanagers = 
```

* Type: string - List of index sub-manager names
* Since: 2014.03
* Since: 2014.09

All items referenced by a product (e.g. texts, prices, media,
etc.) are added to the product index via specialized index
managers. You can add the name of new sub-managers to add more
data to the index or remove existing ones if you don't want to
index that data at all.

This option configures the sub-managers that cares about
indexing data associated to product categories.

See also:

* mshop/index/manager/submanagers

# chunksize

Number of products that should be indexed at once

```
mshop/index/manager/chunksize = 
```

* Type: int - Number of products
* Since: 2014.09

When rebuilding the product index, several products are updated at
once within a transaction. This speeds up the time that is needed
for reindexing.

Usually, the more products are updated in one bunch, the faster the
process of rebuilding the index will be up to a certain limit. The
downside of big bunches is a higher memory consumption that can
exceed the maximum allowed memory of the process.

See also:

* mshop/index/manager/domains
* mshop/index/manager/index
* mshop/index/manager/subdomains
* mshop/index/manager/submanagers

# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/count/ansi = 
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

* mshop/index/manager/search/ansi
* mshop/index/manager/optimize/ansi
* mshop/index/manager/aggregate/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/count/mysql = 
```


See also:

* mshop/index/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the index manager

```
mshop/index/manager/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2015.11

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the index manager.

```
 mshop/index/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the index manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/decorators/global
* mshop/index/manager/decorators/local

## global

Adds a list of globally available decorators only to the index manager

```
mshop/index/manager/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2015.11

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the index manager.

```
 mshop/index/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the index manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/decorators/excludes
* mshop/index/manager/decorators/local

## local

Adds a list of local decorators only to the index manager

```
mshop/index/manager/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2015.11

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Index\Manager\Decorator\*") around the index manager.

```
 mshop/index/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Index\Manager\Decorator\Decorator2" only to the index
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/decorators/excludes
* mshop/index/manager/decorators/global

# domains

A list of domain names whose items should be retrieved together with the product

```
mshop/index/manager/domains = 
```

* Type: string - List of MShop domain names
* Since: 2014.09

To speed up the indexing process, items like texts, prices, media,
attributes etc. which have been associated to products can be
retrieved together with the products.

Please note that the index submanagers expect that the items
associated to the products are fetched together with the products.
Thus, if you leave out a domain, this information won't be part
of the indexed product and therefore won't be found when searching
the index.

See also:

* mshop/index/manager/chunksize
* mshop/index/manager/index
* mshop/index/manager/subdomains
* mshop/index/manager/submanagers

# name

Class name of the used index manager implementation

```
mshop/index/manager/name = 
```

* Type: string - Last part of the class name
* Since: 2015.11

Each default manager can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Index\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Index\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/index/manager/name = Mymanager
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyManager"!


# optimize
## ansi

Optimizes the stored product data for retrieving the records faster

```
mshop/index/manager/optimize/ansi = 
```

* Type: string - SQL statement for optimizing the stored product data
* Since: 2014.09

The SQL statement should reorganize the data in the DBMS storage to
optimize access to the records of the table or tables. Some DBMS
offer specialized statements to optimize indexes and records. This
statement doesn't return any records.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/count/ansi
* mshop/index/manager/search/ansi
* mshop/index/manager/aggregate/ansi

## mysql

Optimizes the stored product data for retrieving the records faster

```
mshop/index/manager/optimize/mysql = 
```


See also:

* mshop/index/manager/optimize/ansi

# price
## cleanup/ansi

Deletes the index price records that haven't been touched

```
mshop/index/manager/price/cleanup/ansi = 
```

* Type: string - SQL statement for deleting the outdated price index records
* Since: 2014.03

During the rebuild process of the product index, the entries of all
active products will be removed and readded. Thus, no stale data for
these products will remain in the database.

All products that have been disabled since the last rebuild will be
still part of the index. The cleanup statement removes all records
that belong to products that haven't been touched during the index
rebuild because these are the disabled ones.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/price/count/ansi
* mshop/index/manager/price/delete/ansi
* mshop/index/manager/price/insert/ansi
* mshop/index/manager/price/search/ansi

## cleanup/mysql

Deletes the index price records that haven't been touched

```
mshop/index/manager/price/cleanup/mysql = 
```


See also:

* mshop/index/manager/price/cleanup/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/price/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the product index
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

* mshop/index/manager/price/search/ansi
* mshop/index/manager/price/optimize/ansi
* mshop/index/manager/price/aggregate/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/price/count/mysql = 
```


See also:

* mshop/index/manager/price/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the index price manager

```
mshop/index/manager/price/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the index price manager.

```
 mshop/index/manager/price/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the index price manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/price/decorators/global
* mshop/index/manager/price/decorators/local

## decorators/global

Adds a list of globally available decorators only to the index price manager

```
mshop/index/manager/price/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the index price
manager.

```
 mshop/index/manager/price/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the index
price manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/price/decorators/excludes
* mshop/index/manager/price/decorators/local

## decorators/local

Adds a list of local decorators only to the index price manager

```
mshop/index/manager/price/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Index\Manager\Price\Decorator\*") around the index
price manager.

```
 mshop/index/manager/price/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Index\Manager\Price\Decorator\Decorator2" only to the
index price manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/price/decorators/excludes
* mshop/index/manager/price/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/price/delete/ansi = 
```

* Type: string - SQL statement for deleting index price records
* Since: 2014.03

Removes the records specified by the given IDs from the index database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/price/count/ansi
* mshop/index/manager/price/cleanup/ansi
* mshop/index/manager/price/insert/ansi
* mshop/index/manager/price/search/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/price/delete/mysql = 
```


See also:

* mshop/index/manager/price/delete/ansi

## insert/ansi

Inserts a new price record into the product index database

```
mshop/index/manager/price/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2014.03

During the product index rebuild, prices related to a product
will be stored in the index for this product. All records
are deleted before the new ones are inserted.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the rebuild() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/price/cleanup/ansi
* mshop/index/manager/price/delete/ansi
* mshop/index/manager/price/search/ansi
* mshop/index/manager/price/count/ansi

## insert/mysql

Inserts a new price record into the product index database

```
mshop/index/manager/price/insert/mysql = 
```


See also:

* mshop/index/manager/price/insert/ansi

## name

Class name of the used index price manager implementation

```
mshop/index/manager/price/name = 
```

* Type: string - Last part of the class name
* Since: 2014.03

Each default index price manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Index\Manager\Price\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Index\Manager\Price\Myprice
```

then you have to set the this configuration option:

```
 mshop/index/manager/price/name = Myprice
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyPrice"!


## optimize/ansi

Optimizes the stored price data for retrieving the records faster

```
mshop/index/manager/price/optimize/ansi = 
```

* Type: string - SQL statement for optimizing the stored price data
* Since: 2014.09

The SQL statement should reorganize the data in the DBMS storage to
optimize access to the records of the table or tables. Some DBMS
offer specialized statements to optimize indexes and records. This
statement doesn't return any records.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/price/count/ansi
* mshop/index/manager/price/search/ansi
* mshop/index/manager/price/aggregate/ansi

## optimize/mysql

Optimizes the stored price data for retrieving the records faster

```
mshop/index/manager/price/optimize/mysql = 
```


See also:

* mshop/index/manager/price/optimize/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/price/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the product index
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

* mshop/index/manager/price/count/ansi
* mshop/index/manager/price/optimize/ansi
* mshop/index/manager/price/aggregate/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/price/search/mysql = 
```


See also:

* mshop/index/manager/price/search/ansi

## submanagers

A list of sub-manager names used for indexing associated items to prices

```
mshop/index/manager/price/submanagers = 
```

* Type: string - List of index sub-manager names
* Since: 2014.03
* Since: 2014.09

All items referenced by a product (e.g. texts, prices, media,
etc.) are added to the product index via specialized index
managers. You can add the name of new sub-managers to add more
data to the index or remove existing ones if you don't want to
index that data at all.

This option configures the sub-managers that cares about
indexing data associated to product prices.

See also:

* mshop/index/manager/submanagers

## types

Use different product prices types for indexing

```
mshop/index/manager/price/types = 
```

* Type: array - List of price types codes
* Since: 2019.04

In some cases, prices are stored with different types, eg. price per kg.
This configuration option defines which types are incorporated in which
order. If a price of the defined type with the lowest index is available,
it will be indexed, otherwise the next lowest index price type. It is
highly recommended to add the price type 'default' with the highest index.


# resource

Name of the database connection resource to use

```
mshop/index/manager/resource = 
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
mshop/index/manager/search/ansi = 
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

* mshop/index/manager/count/ansi
* mshop/index/manager/optimize/ansi
* mshop/index/manager/aggregate/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/search/mysql = 
```


See also:

* mshop/index/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/index/manager/sitemode = 
```

* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole index domain if items from parent sites are inherited,
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

A list of sub-manager names used for indexing associated items

```
mshop/index/manager/submanagers = 
```

* Type: string - List of index sub-manager names
* Since: 2016.02

All items referenced by a product (e.g. texts, prices, media,
etc.) are added to the product index via specialized index
managers. You can add the name of new sub-managers to add more
data to the index or remove existing ones if you don't want to
index that data at all.

Caution: Please note that the list of sub-manager names should
correspond to the list of domains that are fetched together with
the products as the sub-manager depends on the items being
retrieved there and fetching items that won't be indexed is a
waste of resources.

See also:

* mshop/index/manager/submanagers
* mshop/index/manager/chunksize
* mshop/index/manager/domains
* mshop/index/manager/index
* mshop/index/manager/subdomains

# supplier
## cleanup/ansi

Deletes the index supplier records that haven't been touched

```
mshop/index/manager/supplier/cleanup/ansi = 
```

* Type: string - SQL statement for deleting the outdated index records
* Since: 2018.07

During the rebuild process of the product index, the entries of all
active products will be removed and readded. Thus, no stale data for
these products will remain in the database.

All products that have been disabled since the last rebuild will be
still part of the index. The cleanup statement removes all records
that belong to products that haven't been touched during the index
rebuild because these are the disabled ones.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/supplier/count/ansi
* mshop/index/manager/supplier/delete/ansi
* mshop/index/manager/supplier/insert/ansi
* mshop/index/manager/supplier/search/ansi

## cleanup/mysql

Deletes the index supplier records that haven't been touched

```
mshop/index/manager/supplier/cleanup/mysql = 
```


See also:

* mshop/index/manager/supplier/cleanup/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/supplier/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2018.07

Counts all records matched by the given criteria from the product index
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

* mshop/index/manager/supplier/search/ansi
* mshop/index/manager/supplier/optimize/ansi
* mshop/index/manager/supplier/aggregate/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/supplier/count/mysql = 
```


See also:

* mshop/index/manager/supplier/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the index supplier manager

```
mshop/index/manager/supplier/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the index supplier manager.

```
 mshop/index/manager/supplier/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the index supplier manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/supplier/decorators/global
* mshop/index/manager/supplier/decorators/local

## decorators/global

Adds a list of globally available decorators only to the index supplier manager

```
mshop/index/manager/supplier/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the index supplier
manager.

```
 mshop/index/manager/supplier/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the index
supplier manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/supplier/decorators/excludes
* mshop/index/manager/supplier/decorators/local

## decorators/local

Adds a list of local decorators only to the index supplier manager

```
mshop/index/manager/supplier/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2018.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Index\Manager\Supplier\Decorator\*") around the index
supplier manager.

```
 mshop/index/manager/supplier/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Index\Manager\Supplier\Decorator\Decorator2" only to the
index supplier manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/supplier/decorators/excludes
* mshop/index/manager/supplier/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/supplier/delete/ansi = 
```

* Type: string - SQL statement for deleting index supplier records
* Since: 2018.07

Removes the records specified by the given IDs from the index database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/supplier/count/ansi
* mshop/index/manager/supplier/cleanup/ansi
* mshop/index/manager/supplier/insert/ansi
* mshop/index/manager/supplier/search/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/supplier/delete/mysql = 
```


See also:

* mshop/index/manager/supplier/delete/ansi

## insert/ansi

Inserts a new supplier record into the product index database

```
mshop/index/manager/supplier/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2018.07

During the product index rebuild, categories related to a
product will be stored in the index for this product. All
records are deleted before the new ones are inserted.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the rebuild() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/supplier/cleanup/ansi
* mshop/index/manager/supplier/delete/ansi
* mshop/index/manager/supplier/search/ansi
* mshop/index/manager/supplier/count/ansi

## insert/mysql

Inserts a new supplier record into the product index database

```
mshop/index/manager/supplier/insert/mysql = 
```


See also:

* mshop/index/manager/supplier/insert/ansi

## name

Class name of the used index supplier manager implementation

```
mshop/index/manager/supplier/name = 
```

* Type: string - Last part of the class name
* Since: 2018.07

Each default index supplier manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Index\Manager\Supplier\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Index\Manager\Supplier\Mysupplier
```

then you have to set the this configuration option:

```
 mshop/index/manager/supplier/name = Mysupplier
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MySupplier"!


## optimize/ansi

Optimizes the stored supplier data for retrieving the records faster

```
mshop/index/manager/supplier/optimize/ansi = 
```

* Type: string - SQL statement for optimizing the stored supplier data
* Since: 2018.07

The SQL statement should reorganize the data in the DBMS storage to
optimize access to the records of the table or tables. Some DBMS
offer specialized statements to optimize indexes and records. This
statement doesn't return any records.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/supplier/count/ansi
* mshop/index/manager/supplier/search/ansi
* mshop/index/manager/supplier/aggregate/ansi

## optimize/mysql

Optimizes the stored supplier data for retrieving the records faster

```
mshop/index/manager/supplier/optimize/mysql = 
```


See also:

* mshop/index/manager/supplier/optimize/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/supplier/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2018.07

Fetches the records matched by the given criteria from the product index
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

* mshop/index/manager/supplier/count/ansi
* mshop/index/manager/supplier/optimize/ansi
* mshop/index/manager/supplier/aggregate/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/supplier/search/mysql = 
```


See also:

* mshop/index/manager/supplier/search/ansi

## submanagers

A list of sub-manager names used for indexing associated items to categories

```
mshop/index/manager/supplier/submanagers = 
```

* Type: string - List of index sub-manager names
* Since: 2018.07
* Since: 2018.07

All items referenced by a product (e.g. texts, prices, media,
etc.) are added to the product index via specialized index
managers. You can add the name of new sub-managers to add more
data to the index or remove existing ones if you don't want to
index that data at all.

This option configures the sub-managers that cares about
indexing data associated to product categories.

See also:

* mshop/index/manager/submanagers

# text
## attribute-types

List of attribute types that should be added to the product index

```
mshop/index/manager/text/attribute-types = 
```

* Type: array|string|null - Type name or list of type names, null for all
* Since: 2020.10

By default, hidden attributes are not displayed. This setting
allows you to name only those attribute types that should be added. All
others will be left out so products won't be found if users search
for words that are part of those skipped attributes.


## cleanup/ansi

Deletes the index text records that haven't been touched

```
mshop/index/manager/text/cleanup/ansi = 
```

* Type: string - SQL statement for deleting the outdated text index records
* Since: 2014.03

During the rebuild process of the product index, the entries of all
active products will be removed and readded. Thus, no stale data for
these products will remain in the database.

All products that have been disabled since the last rebuild will be
still part of the index. The cleanup statement removes all records
that belong to products that haven't been touched during the index
rebuild because these are the disabled ones.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/text/count/ansi
* mshop/index/manager/text/delete/ansi
* mshop/index/manager/text/insert/ansi
* mshop/index/manager/text/search/ansi
* mshop/index/manager/text/text/ansi

## cleanup/mysql

Deletes the index text records that haven't been touched

```
mshop/index/manager/text/cleanup/mysql = 
```


See also:

* mshop/index/manager/text/cleanup/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/text/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the product index
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

* mshop/index/manager/text/aggregate/ansi
* mshop/index/manager/text/cleanup/ansi
* mshop/index/manager/text/insert/ansi
* mshop/index/manager/text/optimize/ansi
* mshop/index/manager/text/search/ansi
* mshop/index/manager/text/text/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/index/manager/text/count/mysql = 
```


See also:

* mshop/index/manager/text/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the index text manager

```
mshop/index/manager/text/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the index text manager.

```
 mshop/index/manager/text/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the index text manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/text/decorators/global
* mshop/index/manager/text/decorators/local

## decorators/global

Adds a list of globally available decorators only to the index text manager

```
mshop/index/manager/text/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the index text
manager.

```
 mshop/index/manager/text/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the index
text manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/text/decorators/excludes
* mshop/index/manager/text/decorators/local

## decorators/local

Adds a list of local decorators only to the index text manager

```
mshop/index/manager/text/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Index\Manager\Text\Decorator\*") around the index text
manager.

```
 mshop/index/manager/text/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Index\Manager\Text\Decorator\Decorator2" only to the index
text manager.

See also:

* mshop/common/manager/decorators/default
* mshop/index/manager/text/decorators/excludes
* mshop/index/manager/text/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/text/delete/ansi = 
```

* Type: string - SQL statement for deleting index text records
* Since: 2014.03

Removes the records specified by the given IDs from the index database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/text/count/ansi
* mshop/index/manager/text/cleanup/ansi
* mshop/index/manager/text/insert/ansi
* mshop/index/manager/text/search/ansi
* mshop/index/manager/text/text/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/index/manager/text/delete/mysql = 
```


See also:

* mshop/index/manager/text/delete/ansi

## insert/ansi

Inserts a new text record into the product index database

```
mshop/index/manager/text/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2014.03

During the product index rebuild, texts related to a product
will be stored in the index for this product. All records
are deleted before the new ones are inserted.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the rebuild() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/text/cleanup/ansi
* mshop/index/manager/text/count/ansi
* mshop/index/manager/text/delete/ansi
* mshop/index/manager/text/insert/ansi
* mshop/index/manager/text/search/ansi
* mshop/index/manager/text/text/ansi

## insert/mysql

Inserts a new text record into the product index database

```
mshop/index/manager/text/insert/mysql = 
```


See also:

* mshop/index/manager/text/insert/ansi

## name

Class name of the used index text manager implementation

```
mshop/index/manager/text/name = 
```

* Type: string - Last part of the class name
* Since: 2014.03

Each default index text manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Index\Manager\Text\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Index\Manager\Text\Mytext
```

then you have to set the this configuration option:

```
 mshop/index/manager/text/name = Mytext
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyText"!


## optimize/ansi

Optimizes the stored text data for retrieving the records faster

```
mshop/index/manager/text/optimize/ansi = 
```

* Type: string - SQL statement for optimizing the stored text data
* Since: 2014.09

The SQL statement should reorganize the data in the DBMS storage to
optimize access to the records of the table or tables. Some DBMS
offer specialized statements to optimize indexes and records. This
statement doesn't return any records.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/index/manager/text/aggregate/ansi
* mshop/index/manager/text/cleanup/ansi
* mshop/index/manager/text/count/ansi
* mshop/index/manager/text/insert/ansi
* mshop/index/manager/text/search/ansi
* mshop/index/manager/text/text/ansi

## optimize/mysql

Optimizes the stored text data for retrieving the records faster

```
mshop/index/manager/text/optimize/mysql = 
```


See also:

* mshop/index/manager/text/optimize/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/text/search/ansi = 
```

* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the product index
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

* mshop/index/manager/text/aggregate/ansi
* mshop/index/manager/text/cleanup/ansi
* mshop/index/manager/text/count/ansi
* mshop/index/manager/text/insert/ansi
* mshop/index/manager/text/optimize/ansi
* mshop/index/manager/text/text/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/index/manager/text/search/mysql = 
```


See also:

* mshop/index/manager/text/search/ansi

## submanagers

A list of sub-manager names used for indexing associated items to texts

```
mshop/index/manager/text/submanagers = 
```

* Type: string - List of index sub-manager names
* Since: 2014.03
* Since: 2014.09

All items referenced by a product (e.g. texts, prices, media,
etc.) are added to the product index via specialized index
managers. You can add the name of new sub-managers to add more
data to the index or remove existing ones if you don't want to
index that data at all.

This option configures the sub-managers that cares about
indexing data associated to product texts.

See also:

* mshop/index/manager/submanagers

## types

List of text types that should be added to the product index

```
mshop/index/manager/text/types = 
```

* Type: array|string|null - Type name or list of type names, null for all
* Since: 2019.04

By default, all available texts of a product are indexed. This setting
allows you to name only those text types that should be added. All
others will be left out so products won't be found if users search
for words that are part of those skipped texts. This is most useful
for avoiding product matches due to texts that should be internal only.
