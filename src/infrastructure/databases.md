The Aimeos core is database independent and supports several relational databases. For creating the database schema it uses the [Doctrine DBAL](https://docs.doctrine-project.org/projects/doctrine-dbal/en/latest/index.html) layer. For retrieving, saving and deleting data, ANSI compatible SQL statements are used which can be replaced by database specific ones if necessary.

For details about the structure of the Aimeos database, please have a look at the SVG file of the [ERM diagram for the Aimeos database layout](https://aimeos.org/fileadmin/download/Aimeos-database.svgz).

Aimeos supports multiple database servers for storing the data required by the shop.

Fully supported are:

* MySQL (adapter: "mysql", version: 5.7.8+)
* PostgreSQL (adapter: "pgsql", version: 9.5+)
* Microsoft SQL Server (adapter: "sqlsrv", version: 2017+)

Basic support is included for:

* IBM DB2 (adapter: "db2")
* Oracle (adapter: "oracle", version: 8+)
* SAP SQL Anywhere (adapter: "sqlanywhere", version: 10+)

Basic support means that the required functionality is implemented but not continuously tested and without performance optimized searching.

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
