
# cleanup

```
madmin/cache/manager/cleanup = DELETE FROM "madmin_cache" WHERE "expire" < ?
```

* Default: 


# clear

```
madmin/cache/manager/clear = DELETE FROM "madmin_cache"
```

* Default: 


# count
## ansi

Retrieves the records matched by the given criteria in the database

```
madmin/cache/manager/count/ansi = 
```

* Default: 
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the cache
database. The records must be from the sites that is
configured in the context item.

To limit the records matched, conditions can be added to the given
criteria object. It can contain comparisons like column names that
must match specific values which can be combined by AND, OR or NOT
operators. The resulting string of SQL conditions replaces the
":cond" placeholder before the statement is sent to the database
server.

Contrary to the "search" statement, it doesn't return any records
but instead the number of records that have been found. As counting
thousands of records can be a long running task, the maximum number
of counted records is limited for performance reasons.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/cache/manager/get/ansi
* madmin/cache/manager/delete/ansi
* madmin/cache/manager/deletebytag/ansi
* madmin/cache/manager/set/ansi
* madmin/cache/manager/settag/ansi
* madmin/cache/manager/search/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
madmin/cache/manager/count/mysql = 
```

* Default: 

See also:

* madmin/cache/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the cache manager

```
madmin/cache/manager/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. cache what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for cacheged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"madmin/common/manager/decorators/default" before they are wrapped
around the cache manager.

```
 madmin/cache/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"madmin/common/manager/decorators/default" for the cache manager.

See also:

* madmin/common/manager/decorators/default
* madmin/cache/manager/decorators/global
* madmin/cache/manager/decorators/local

## global

Adds a list of globally available decorators only to the cache manager

```
madmin/cache/manager/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. cache what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for cacheged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the cache manager.

```
 madmin/cache/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the cache controller.

See also:

* madmin/common/manager/decorators/default
* madmin/cache/manager/decorators/excludes
* madmin/cache/manager/decorators/local

## local

Adds a list of local decorators only to the cache manager

```
madmin/cache/manager/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. cache what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for cacheged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the cache manager.

```
 madmin/cache/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator2" only to the cache
controller.

See also:

* madmin/common/manager/decorators/default
* madmin/cache/manager/decorators/excludes
* madmin/cache/manager/decorators/global

# delete

```
madmin/cache/manager/delete = DELETE FROM "madmin_cache" WHERE "id" IN (?)
```

* Default: 


# deletebytag

```
madmin/cache/manager/deletebytag = 
 DELETE FROM "madmin_cache" WHERE "id" IN (
 	SELECT "tid" FROM "madmin_cache_tag" WHERE "tname" IN (?)
 )
```

* Default: 


# get

```
madmin/cache/manager/get = 
 SELECT "id", "value", "expire" FROM "madmin_cache"
 WHERE ( "expire" >= ? OR "expire" IS NULL ) AND "id" IN (?)
```

* Default: 


# name

Class name of the used cache manager implementation

```
madmin/cache/manager/name = Standard
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
 \Aimeos\MShop\Cache\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Cache\Manager\Mymanager
```

then you have to set the this configuration option:

```
 madmin/cache/manager/name = Mymanager
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyManager"!


# search
## ansi

Retrieves the records matched by the given criteria in the database

```
madmin/cache/manager/search/ansi = 
 SELECT "id", "value", "expire"
 FROM "madmin_cache"
 WHERE :cond
 ORDER BY "id"
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: madmin/cache/manager/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the cache
database. The records must be from the sites that is
configured in the context item.

To limit the records matched, conditions can be added to the given
criteria object. It can contain comparisons like column names that
must match specific values which can be combined by AND, OR or NOT
operators. The resulting string of SQL conditions replaces the
":cond" placeholder before the statement is sent to the database
server.

The number of returned records can be limited and can start at any
number between the begining and the end of the result set. For that
the ":size" and ":start" placeholders are replaced by the
corresponding values from the criteria object. The default values
are 0 for the start and 100 for the size value.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/cache/manager/get/ansi
* madmin/cache/manager/delete/ansi
* madmin/cache/manager/deletebytag/ansi
* madmin/cache/manager/set/ansi
* madmin/cache/manager/settag/ansi
* madmin/cache/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
madmin/cache/manager/search/mysql = 
 SELECT "id", "value", "expire"
 FROM "madmin_cache"
 WHERE :cond
 ORDER BY "id"
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT "id", "value", "expire"
 FROM "madmin_cache"
 WHERE :cond
 ORDER BY "id"
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* madmin/cache/manager/search/ansi

# set

```
madmin/cache/manager/set = 
 INSERT INTO "madmin_cache" (
 	"id", "expire", "value"
 ) VALUES (
 	?, ?, ?
 )
```

* Default: 


## ansi

Inserts the cache entry into the database

```
madmin/cache/manager/set/ansi = 
```

* Default: 
* Type: string - SQL statement for inserting a new cache entry
* Since: 2014.03

The ID, value and expiration timestamp are inserted as new record
into the cache database. Any existing record must be deleted before
the new one can be inserted.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the cache item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the set() method, so the correct values are bound to the
columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/cache/manager/delete/ansi
* madmin/cache/manager/deletebytag/ansi
* madmin/cache/manager/get/ansi
* madmin/cache/manager/settag/ansi
* madmin/cache/manager/search/ansi
* madmin/cache/manager/count/ansi

## mysql

Inserts the cache entry into the database

```
madmin/cache/manager/set/mysql = 
```

* Default: 

See also:

* madmin/cache/manager/set/ansi

# settag

```
madmin/cache/manager/settag = 
 INSERT INTO "madmin_cache_tag" (
 	"tid", "tname"
 ) VALUES (
 	?, ?
 )
```

* Default: 


## ansi

Inserts a new tag to an existing cache entry

```
madmin/cache/manager/settag/ansi = 
```

* Default: 
* Type: string - SQL statement for inserting a new tag to an existing cache entry
* Since: 2014.03

The ID of the cache entry and the tag name are inserted as a new
record into the cache database. Any existing tag record that
conflicts with the new one must be deleted before it can be inserted.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the cache ID and tag name from the cache item to the statement
before they are sent to the database server. The number of question
marks must be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the order in
the save() method, so the correct values are bound to the
columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/cache/manager/delete/ansi
* madmin/cache/manager/deletebytag/ansi
* madmin/cache/manager/get/ansi
* madmin/cache/manager/set/ansi
* madmin/cache/manager/search/ansi
* madmin/cache/manager/count/ansi

## mysql

Inserts a new tag to an existing cache entry

```
madmin/cache/manager/settag/mysql = 
```

* Default: 

See also:

* madmin/cache/manager/settag/ansi

# submanagers

List of manager names that can be instantiated by the cache manager

```
madmin/cache/manager/submanagers = Array
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
