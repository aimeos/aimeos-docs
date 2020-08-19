The Aimeos core is database independent and supports several relational databases. For creating the database schema it uses the [Doctrine DBAL](http://docs.doctrine-project.org/projects/doctrine-dbal/en/latest/index.html) layer. For retrieving, saving and deleting data, ANSI compatible SQL statements are used which can be replaced by database specific ones if necessary.

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

Basic support means that the required functionality is implemented but not continuously tested.

# Specific DBMS settings

## MySQL

For MySQL you don't need to change any configuration values in the Aimeos settings.

Nevertheless, there's one optional optimization:
The [innodb_flush_log_at_trx_commit](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit) default setting for the InnoDB storage engine can lead to a massive performance loss. This can happen if a lot of information is written to the cache tables and each INSERT/DELETE/UPDATE is followed by a `fsync()` which flushes the dirty pages to the hard disk and this is very slow.

If you set the value for `innodb_flush_log_at_trx_commit` to something else than the default value (which is "1"), then `fsync()` is called only every second.

```
innodb_flush_log_at_trx_commit = 2
```

!!! note
    The downside is that the system isn't ACID compliant any more and you will loose all writes of the last second when the server crashes. A value of "2" is a little bit safer than "0" because then you will only loose the last writes if the hardware or the operating system crashes and not if only the MySQL daemon dies.

## PostgreSQL

For PostgreSQL servers, you need to reset some configuration and configure PostgreSQL specific classes for maximum performance:

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
            'attribute' => [
                'name' => 'Standard',
            ],
            'catalog' => [
                'name' => 'Standard',
            ],
            'price' => [
                'name' => 'Standard',
            ],
            'supplier' => [
                'name' => 'Standard',
            ],
            'text' => [
                'name' => 'PgSQL',
            ],
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
            'name' => 'Standard',
            'attribute' => [
                'name' => 'Standard',
            ],
            'catalog' => [
                'name' => 'Standard',
            ],
            'price' => [
                'name' => 'Standard',
            ],
            'text' => [
                'name' => 'SQLSrv',
            ],
        ],
    ],
],
```

# Multiple databases

The Aimeos e-commerce components are able to use different databases for its data domains. Thus, you can configure a separate database e.g. for all customer or order related data. These database can even use different database servers like MySQL, PostgreSQL, Oracle, SQL Server, etc. If no specific database is configured for a data domain, the default database will be used.

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
    Usually it doesn't make sense to put every data domain into an own database. Reasonable data domains are those which will grow very big in your setup. Candidates are the **log** and **order** domains which might fill up with data over the time.

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

You can add an entry for every data domain replacing the *<domain>* placeholder in the example above with the name of the data domain. For the customer data domain it would be e.g.

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

The fallback database (which is also the standard database) is already configured within the Aimeos TYPO3 extension and is the one of your TYPO3 installation. If you want to move the shop related tables to their own database, add a configuration entry for **db** to your configuration file:

```php
	'db' => [
		// ...
	],
```

!!! warning
    During a request, only one database connection per configured database should be open. Limiting the maximum connections to "1" works until you try to execute run the setup tasks as some of them need two connections to for reading and writing in parallel.
