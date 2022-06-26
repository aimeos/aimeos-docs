The Aimeos core is database independent and supports several relational databases for storing the data required by the shop.

Fully supported are:

* MySQL (adapter: "mysql", version: 5.7.8+)
* PostgreSQL (adapter: "pgsql", version: 9.5+)
* Microsoft SQL Server (adapter: "sqlsrv", version: 2017+)

Basic support is included for:

* IBM DB2 (adapter: "db2")
* Oracle (adapter: "oracle", version: 8+)
* SAP SQL Anywhere (adapter: "sqlanywhere", version: 10+)

Basic support means that the required functionality is implemented but not continuously tested and without performance optimized searching.

For creating and updating the database schema as well as migrating the data the Aimeos Core uses [Upscheme](https://upscheme.org). ANSI compatible SQL statements are used for retrieving, saving and deleting data, which can be replaced by database specific ones if necessary.

For details about the Aimeos database structure, please have a look at the SVG file of the [ERM diagram for the Aimeos database layout](https://aimeos.org/fileadmin/download/Aimeos-database.svgz).

# Low-level API

When implementing [managers](../models/managing-items.md) for retrieving and storing data, you need to execute SQL statements by using the Aimeos database object. The Aimeos [context](context.md) contains the database manager object which returns the requested database connection.

## Get connections

To retrieve the standard database connection, use the `db()` method without parameters:

```php
// default database connection
$conn = $context->db();
```

This database does always exist but may not contain the tables you want to modify or query because in Aimeos, each data domain like attribute, catalog, media, price, product, service, text, etc. can be stored in a separate database. To get the database connection for a specific data domain instead, pass `db-<domain>` as first parameter:

```php
// specific database connection
$conn = $context->db( 'db-product' );
```

This will always return the database connection containing the `mshop_product` and related tables. If there's no extra database for the product domain configured, it returns the default connection instead.

While retrieving rows, you can't update data using the same connection because you need two connections for that. If you pass `true` as second parameter to the `db()` method of the context, it will return a new connection instead of the existing one:

```php
// first connection
$conn = $context->db( 'db-product' );

// 2nd database connection (new)
$conn2 = $context->db( 'db-product', true );

// execute query
$result = $conn->query( 'SELECT "id", "label" FROM "mshop_product"' );

// prepare update statement
$stmt = $conn2->create( 'UPDATE "mshop_product" SET "label"=? WHERE "id"=?' );

// retrieve rows
while( $row = $result->fetch() ) {

    // update rows
    $stmt->bind( 1, ucwords( $row['label'] ) )
        ->bind( 2 $row['id'], \Aimeos\Base\DB\Statement\Base::PARAM_INT )
        ->execute()
        ->finish();
}

// close 2nd connection again
$conn2->close()
```

It's important to close the second connection at the end because otherwise, they will pile up until the script terminates or the database server refuses to accept new connections.

!!! warning
    Don't close the first connection to avoid slowing down your application by frequent reconnects to the database!

## Simple statements

For standard insert, update, delete and query operations, you can use the shortcut methods offered by the connection object. They only require the table name and the parameters and/or conditions as column/value pairs.

!!! note
    If you have statements that only need to be executed once, these methods are fine. Otherwise, use custom statements where you create the statement once and only bind different values for each execution.

### Insert

To add a new row, pass the table name as first parameter as well as an associative list of column names and their values to the `insert()` method:

```php
$result = $context->db()->insert(
    'mshop_product',
    ['siteid' => '1.', 'code' => 'test', 'label' => 'Test product']
);
```

The returned result object allows you to call `affectedRows()` for the number of inserted rows but it may or may not return any value depending on the database server implementation.

### Update

For updating existing rows, pass the table name as first parameter, an associative list of column names and their values which should be changed as second parameter and an associative list of column names and their values for the conditions as third parameter:

```php
$result = $context->db()->update(
    'mshop_product',
    ['status' => 1],
    ['code' => 'test']
);
```

The conditions are optional and if you skip them, all rows in the table will be changed.

The returned result object allows you to call `affectedRows()` for the number of inserted rows but it may or may not return any value depending on the database server implementation.

### Delete

To delete existing rows, pass the table name as first parameter and an associative list of column names and their values for the conditions as second parameter:

```php
$result = $context->db()->delete(
    'mshop_product',
    ['code' => 'test']
);
```

The conditions are optional and if you skip them, all rows in the table will be deleted.

The returned result object allows you to call `affectedRows()` for the number of inserted rows but it may or may not return any value depending on the database server implementation.

### Query

The `query()` method fetches rows from the database server and besides the SQL statement as first parameter, you can pass the values for the placeholders (`?`) used in the SQL as second parameter:

```php
$result = $context->db()->query(
    'SELECT * FROM "mshop_product" WHERE "code"=?',
    ['test']
);
```

!!! note
    You are responsible for quoting any identifier (table or column name, etc.) with double quotes yourself!

!!! note
    The type of the parameter is determined by the type of the PHP variable, so make sure you've casted the values accordingly before passing them to the `query()` method!

Afterwards, you can get the rows using the `fetch()` method:

```php
while( $row = $result->fetch() ) {
    // $row['id'], $row['code'], ...
}
```

!!! warning
    Always fetch all rows until `$result->fetch()` returns NULL or execute `$result->finish()` if you are unsure! Otherwise, the outstanding rows will be returned by the next `fetch()` call even if you've executed a different SELECT statement in the meantime.

A short alternative to get all rows at once, but usually less efficient:

```php
$rows = $result->all();
```

## Custom statements

Simple statements don't allow joining tables and also doesn't support other advanced database features. Then, custom statements are the only option.

First, you need the connection like before:

```php
$conn = $context->db();
```

If your SQL statement contains any table or column names that are not fixed strings, you must quote them using the `qi()` method:

```php
$col = $conn->qi( 'type' );
```

If you don't, your application is vulnerable to SQL injection attacks!

Create a prepared statement from the resulting SQL string, which can contain placeholders (`?`) for binding the values later:

```php
$sql = 'SELECT COUNT(*)
    FROM "mshop_product"
    WHERE "id" < ? AND "datestart" >= ?
    GROUP BY ' . $col;
$stmt = $conn->create( $sql );
```

Each placeholder (`?`) must be bound to a value using the `bind()` method. The first parameter is the index of the placeholder (start at 1), the second the value to bind and the third parameter is the type constant for the value:

```php
$stmt->bind( 1, 1000, \Aimeos\Base\DB\Statement\Base::PARAM_INT );
$stmt->bind( 2, '2000-01-01 00:00:00' );
```

!!! warning
    The placeholder index passed as first parameter starts at 1, not 0!

Available type constants are:

* \Aimeos\Base\DB\Statement\Base::PARAM_NULL : NULL values only
* \Aimeos\Base\DB\Statement\Base::PARAM_BOOL : TRUE/FALSE values
* \Aimeos\Base\DB\Statement\Base::PARAM_INT : Integer numbers
* \Aimeos\Base\DB\Statement\Base::PARAM_FLOAT : Floating point numbers
* \Aimeos\Base\DB\Statement\Base::PARAM_STR : String values
* \Aimeos\Base\DB\Statement\Base::PARAM_LOB : Large objects

If you pass no type constant, `\Aimeos\Base\DB\Statement\Base::PARAM_STR` is used and this can lead to unnecessary type conversions and may slow down the database.

After creating the statement and binding the values, you can send the statement to the database server using `execute()`:

```php
$result = $stmt->execute();
```

The API will return a result object for fetching the rows from the database. Call the `fetch()` method in a loop until it returns NULL to get all rows:

```php
while( $row = $result->fetch() ) {
    // ...
}
```

At last, close the database cursor to ensure that there's no more data (from additional statements) left:

```php
$result->finish();
```

!!! tip
    You can also use the same procedure for INSERT, UPDATE and DELETE statements, but you don't need to call `fetch()` in this case. Instead, you can call `$result->affectedRows()` to get the number of inserted, changed or deleted rows but depending on the database server implementation, this method may return 0 in all cases.

## Transactions

To execute all statements or none at all for consistency, transactions are handy straight forward:

```php
$conn = $context->db();
$conn->begin();

try
{
    if( $conn->inTransaction() ) {
        // yes, we are
    }
    $conn->commit();
}
catch( \Throwable $t )
{
    $conn->rollback();
}
```

You can also stack several transactions but only the last `commit()` or `rollback()` will be sent to the database:

```php
$conn = $context->db();

$conn->begin();
// add rows
$conn->begin();
// more rows but something went wrong
$conn->rollback();
// something else
$conn->commit();
```

This sequence will commit the whole changes because the inner `begin()`/`rollback()` will only increase/decrease the transaction counter and won't have any other consequences.

# Multiple databases

The Aimeos e-commerce components are able to use different databases for their data domains. Thus, you can, e.g., configure a separate database for all customer or order related data. These databases can even use different database servers like MySQL, PostgreSQL, Oracle, SQL Server, etc. If no specific database is configured for a data domain, the default database will be used.

In fact, there are 16 different data domains which can be stored in one database each. These include domains for:

* attribute
* cache
* catalog
* coupon
* customer
* job
* locale
* log
* media
* order
* plugin
* price
* product
* review
* service
* supplier
* text

!!! tip
    Usually it doesn't make sense to assign every data domain to its own database. Reasonable data domains are those which will grow very big in your setup. Candidates are the **log** and **order** domains which might fill up with data over the time.

You need to create a **resource.php** file in the config directory that will contain the database configuration:

```php
<?php
return [
    'db-<domain>' => [
        'adapter' => 'mysql',
        'host' => '<host name or IP address>',
        'port' => '<if a non-standard port is used>',
        'database' => '<database name>',
        'username' => '<name of the database user>',
        'password' => '<secret password for the user>',
        'stmt' => ["SET SESSION sort_buffer_size=2097144; SET NAMES 'utf8mb4'; SET SESSION sql_mode='ANSI'; SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED"],
        'limit' => 2,
        'opt-persistent' => 0
    ],
];
```

You can add an entry for every data domain replacing the *<domain>* placeholder in the example above with the name of the data domain. E.g., for the customer data domain it would be:

```php
    'db-customer' => [
        'adapter' => 'mysql',
        'host' => 'localhost',
        'port' => '3306',
        'database' => 'my_typo3_website',
        'username' => 'myuser',
        'password' => 'secret',
        'stmt' => ["SET SESSION sort_buffer_size=2097144; SET NAMES 'utf8mb4'; SET SESSION sql_mode='ANSI'; SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED"],
        'limit' => 2,
        'opt-persistent' => 0
    ],
```

The fallback database (which is also the standard database) is already configured in your installation. If you want to move the shop related tables to their own database, add a configuration entry for **db** to your configuration file:

```php
    'db' => [
        // ...
    ],
```

!!! warning
    During a request, only one database connection per configured database should be open. Limiting the maximum connections to "1" works until you try to execute the setup tasks, because some of the configured databases need two connections to for reading and writing in parallel.

# Specific DBMS settings

## MySQL

For MySQL you don't need to change any configuration values in the Aimeos settings.

### Search for short words

By default, the MySQL server stores only words with at least four characters into the fulltext index (and only if it's not a stop word). To add shorter words (e.g. with three characters) to the index, you have to adapt the MySQL `ft_min_word_len` setting in the my.cnf configuration file:

```
ft_min_word_len = 3
```

Afterwards, you have to rebuild the fulltext index with

```
REPAIR TABLE mshop_index_text QUICK
```

### MySQL server settings

Depending of the size of the database and the number of rows in the different tables, it might be necessary to adapt some MySQL server settings to get the maximum speed out of Aimeos.

The easiest way to find out if there are any problems caused by e.g. buffers that are too small is by looking at the "Status" tab (or "Show MySQL runtime information" link in older versions) on the home screen of phpMyAdmin. It contains the different server variables that can be changed, their values and a description sometimes including hints what to do. The cool thing about this view is that phpMyAdmin highlights the values in red that may be a source of problems.

Watch out for these keys specifically:

Created_tmp_disk_tables
: The number of temporary tables that have been written to the hard disk because the buffer was too small. See `tmp_table_size` if this happened more than a few times.

Innodb_buffer_pool_reads
: The number of times index data have to be read from the hard disk because it was not cached in memory. High values may indicate the need to increase the value for `innodb_buffer_pool_size`.

Qcache_lowmem_prunes
: The number of queries that had been removed from the query cache because there was no more space left. If this value is high, try to increase `query_cache_size`.

Slow_queries
: The number of queries that need longer than the configured number of seconds. If this value is high, your server is either to slow for the amount of simultaneous users that are hitting your site or there are some very slow queries executed very often. In the later case check, if you've installed extensions for Aimeos that don't scale well and cause performance problems.

Sort_merge_passes
: The number of merge passes the sort algorithm has been forced to do. Higher values can be a hint to increase the `sort_buffer_size`.

These MySQL variables are worth looking out for:

[innodb_buffer_pool_size](http://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size)
: The higher this value, the more data and indexes are available in memory; this is much faster than reading them from the hard disk.

[sort_buffer_size](http://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_sort_buffer_size)
: The buffer size that is available for sorting result sets if no index can be used.

[tmp_table_size](http://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size)
: The size of the in-memory buffer for temporary tables before they are written to the hard disk.

### Write performance

Nevertheless, there's one optional optimization:
The [innodb_flush_log_at_trx_commit](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit) default setting for the InnoDB storage engine can lead to a massive performance loss. This can happen if a lot of information is written to the cache tables and each INSERT/DELETE/UPDATE is followed by a `fsync()` which flushes the dirty pages to the hard disk and this is very slow.

If you set the value for `innodb_flush_log_at_trx_commit` to something else than the default value (which is "1"), then `fsync()` is called only every second.

```
innodb_flush_log_at_trx_commit = 2
```

!!! note
    The downside is that the system isn't ACID compliant any more and you will loose all writes of the last second when the server crashes. A value of "2" is a little bit safer than "0" because then you will only loose the last writes if the hardware or the operating system crashes and not if only the MySQL daemon dies.


### Analyze/optimize tables

MySQL uses the index that fits best to perform the query. This decision is made on the cardinality of the index. Indices with a higher cardinality are preferred over indices with lower ones. Problems arise, when the cardinality is incorrect. Therefore, it's a good idea to check the cardinality values in the `mshop_index_*` tables once in a while, especially if you think the product search is slower than in the past while the number of products is not much higher than before.

To get rid of the problem you have to execute the MySQL

```sql
ANALYZE TABLE "table name"
```

statement, and if it doesn't help, run the MySQL

```sql
OPTIMIZE TABLE "table name"
```

statement afterwards. The statements are also executed after the index rebuild has been finished.

!!! note
    Please be careful with "OPTIMIZE TABLE" if your shop has a large number of records in these index tables, as it hurts performance of the front-end during its execution quite drastically.

### Keep indexes in memory

If you have enough RAM, you should try to keep all indexes in memory to reduce the need to access the hard disc to a minimum. Nevertheless, make sure that the total amount of `key_buffer_size + innodb_buffer_pool_size` does not exceed 75% of the available RAM and that there is enough RAM for the database connections and the operating system.

To find out the size (in MB) of all indexes, use these statements:

```sql
SELECT CEIL( SUM( index_length + data_length ) / POWER( 1024, 2 ) ) innodb_buffer_pool_size_MB
FROM information_schema.tables WHERE engine = 'InnoDB';
```

### Load indexes into RAM

To get the maximum performance that is possible it's necessary to reduce the need to access the hard disc to a minimum. For this, you must have enough RAM to store the indexes of the "mshop_index_*" tables into the MySQL cache.

For InnoDB tables, the `OPTIMIZE TABLE` statement makes sure that all the indexes (and data, since InnoDB stores both in one data structure) of the tables are in the cache if it's big enough:

```sql
OPTIMIZE TABLE mshop_index_attribute
OPTIMIZE TABLE mshop_index_catalog
OPTIMIZE TABLE mshop_index_price
```

If you have plenty of RAM in your database server, you can also load the "mshop_product" and "mshop_product_list" tables:

```sql
OPTIMIZE TABLE mshop_product
OPTIMIZE TABLE mshop_product_list
```

## PostgreSQL

For PostgreSQL servers, you need to reset some configuration options and configure PostgreSQL specific classes for maximum performance:

```php
'resource' => [
    'db' => [
        'adapter' => 'pgsql',
        'host' => '...',
        'port' => '5432',
        'database' => '...',
        'username' => '...',
        'password' => '...',
        'stmt' => [],
    ],
],
'mshop' => [
    'index' => [
        'manager' => [
            'name' => 'PgSQL',
        ],
    ],
],
```

## SQL Server

```php
'resource' => [
    'db' => [
        'adapter' => '...',
        'host' => '...',
        'port' => '...',
        'database' => '...',
        'username' => '...',
        'password' => '...',
        'stmt' => [],
    ],
],
'mshop' => [
    'index' => [
        'manager' => [
            'name' => 'SQLSrv',
        ],
    ],
],
```
