In Aimeos, setup tasks are responsible for creating the database schema, updating the schema if necessary and migrating data required due to schema changes. They have to perform their tasks for all supported databases.

The setup tasks have a lot of advantages and exceed the possibilities of other available solutions like ["Object-relational mapping" (ORM)](https://en.wikipedia.org/wiki/Object-relational_mapping) or similar alternatives to setup tasks:

* The database structure is stored in the version control system
* For every commit there can be a suitable database structure created
* Everyone can update their existing database to a newer version
* Updates are possible from any commit, not only from released versions
* Data transformation is possible via PHP code if SQL is not enough
* They can declare dependencies to other tasks

They are also used to write the default and unit test data to the database during the setup process.

# Schema updates

Updating an existing schema or adding a new table to an existing data domain (product, catalog, attribute, etc.) is very simple and described in this article. If you need to migrate data, want to add a new data domain or rename a table, you need to create your own [setup task](#setup-task).

For already existing data domains, a schema file exists in the [./lib/mshoplib/setup/default/schema/](https://github.com/aimeos/aimeos-core/tree/master/lib/mshoplib/setup/default/schema) directory of the Aimeos core. It consists of the list of tables including their definitions as [Doctring DBAL schema](https://docs.doctrine-project.org/projects/doctrine-dbal/en/latest/). The *attribute.php* file contains these lines for example:

```php
return [
  'table' => [
    'mshop_attribute_type' => function ( \Doctrine\DBAL\Schema\Schema $schema ) {

        $table = $schema->createTable( 'mshop_attribute_type' );

        $table->addColumn( 'id', 'integer', ['autoincrement' => true] );
        $table->addColumn( 'siteid', 'integer', [] );
        $table->addColumn( 'domain', 'string', ['length' => 32] );
        $table->addColumn( 'code', 'string', ['length' => 32] );
        $table->addColumn( 'label', 'string', ['length' => 255] );
        $table->addColumn( 'status', 'smallint', [] );
        $table->addColumn( 'mtime', 'datetime', [] );
        $table->addColumn( 'ctime', 'datetime', [] );
        $table->addColumn( 'editor', 'string', ['length' => 255] );

        $table->setPrimaryKey( ['id'],'pk_msattty_id' );
        $table->addUniqueIndex( ['siteid', 'domain', 'code'],'unq_msattty_sid_dom_code' );
        $table->addIndex( ['siteid', 'status'],'idx_msattty_sid_status' );
        $table->addIndex( ['siteid', 'label'],'idx_msattty_sid_label' );
        $table->addIndex( ['siteid', 'code'],'idx_msattty_sid_code' );

        return $schema;
    },

    // ...
  ],
},
```

The files from the core contains an anonymous function that creates the table, adds the columns and indexes. An important detail is to return the updated schema. This object will then be passed to the anonymous function for the same table in your extension.

!!! warning
    Please remember that identifiers (table/column/index names) must **not be longer then 30 characters**!

## Add new tables

In your own extension, you have to create a PHP file with the same name as the file for the existing data domain, i.e. *attribute.php* in the *./lib/custom/setup/default/schema/* directory. This file can contain one or more anonymous functions for new tables of the same data domain. They are created exactly like in the Aimeos core, e.g.

```php
return [
  'table' => [
    'mshop_attribute_mytable' => function ( \Doctrine\DBAL\Schema\Schema $schema ) {

        $table = $schema->createTable( 'mshop_attribute_mytable' );

        $table->addColumn( 'id', 'integer', ['autoincrement' => true] );
        $table->addColumn( 'siteid', 'integer', [] );
        $table->addColumn( 'myvalue', 'string', ['length' => 255, 'notnull' => false] );
        $table->addColumn( 'mtime', 'datetime', [] );
        $table->addColumn( 'ctime', 'datetime', [] );
        $table->addColumn( 'editor', 'string', ['length' => 255] );

        $table->setPrimaryKey( ['id'],'pk_msattmy_id' );
        $table->addUniqueIndex( ['siteid', 'myvalue'],'unq_msattmy_sid_myval' );

        return $schema;
    },
  ],
);
```

!!! warning
    The array key and the table name must be the same. Also, don't forget to **return the schema object**!

## Tables for new domains

To create tables for a new data domain (not the existing ones like "attribute", "product", "service", etc.], then you need to create a setup task too. This setup task must extend from the existing MShopCreateTables (or MAdminCreateTables) setup task:

```php
namespace Aimeos\MW\Setup\Task;

class TablesCreateMydomain extends TablesCreateMShop
{
    public function getPreDependencies()
    {
        return ['MShopCreateTables', 'MAdminCreateTables'];
    }

    public function getPostDependencies()
    {
        return [];
    }

    public function migrate()
    {
        $this->msg( 'Creating base tables', 0, '' )
        $ds = DIRECTORY_SEPARATOR;

        $files = [
            'db-<mydomain>' => 'default' . $ds . 'schema' . $ds . '<mydomain>.php'
        ];
        $this->setupSchema( $files );
    }
}
```

In the *clean()* and *migrate()* methods, you have to call the *setupSchema()* method from the parent class with the file that contains your schema definition. For *clean()*, the second parameter must be *true* so DBAL will remove old tables, columns and indexes. The *$files* array contains the name of the database connection as key (*db* is used if *db-<mydomain>* isn't explicitely configured) and the relative path to the schema file.

!!! note
    Please replace **<mydomain>** and rename the class by the real name of your new domain.

## Modify existing tables

It's possible to modify schema definitions of core tables in extensions. This enables your extension to add additional columns or indexes to core tables or change column options like their length or type. Your changes will be applied to the tables while the setup tasks are running as long as your extension is installed.

You have to create a PHP file with the same name as the file for the existing data domain, i.e. attribute.php in the *./lib/custom/setup/default/schema/* directory - just like for adding a new table.

The important difference to adding new tables is that the schema object already contains a table definition. You can retrieve the definition by using the *getTable()* method of the schema object. Afterwards, you can use the methods of the [table schema class](https://github.com/doctrine/dbal/blob/master/lib/Doctrine/DBAL/Schema/Table.php) to modify the table according to your needs, e.g.:

```php
return [
  'table' => [
    'mshop_attribute_type' => function ( \Doctrine\DBAL\Schema\Schema $schema ) {

        $table = $schema->getTable( 'mshop_attribute_type' );

        $table->addColumn(  'value', 'string', ['length' => 255] );
        $table->changeColumn(  'value', ['length' => 64] );
        $table->dropColumn(  'value' );

        $table->addIndex( ['value'],'idx_msattty_val' );
        $table->dropIndex( 'unq_msattmy_sid_myval' );
        $table->renameIndex( 'unq_msattmy_sid_myval', 'unq_msattmy_sid_myval_new' );

        return $schema;
    },
  ],
);
```

!!! warning
    The array key and the table name must be the same. Also, don't forget to **return the schema object**!

## Platform specific

Sometimes you might need to use column or index options that are only available for specific database servers, e.g. a MySQL fulltext index. While you can create those indexes without problems in your own setup task, DBAL would try to change your column or index during every setup run.

The solution is to list the identifiers of those platform specific indexes in the exclude section of the same file, e.g. in the *attribute.php* file located in the *./lib/custom/setup/default/schema/* directory:

```php
return [
  'exclude' => [
    'idx_msindte_value',
  ],

  'table' => [
    // ...
  )
);
```

This will leave the index with the name *idx_msindte_value* untouched by DBAL if its part of a table in the same data domain.

# Setup process

There can be several directories which contain *setup tasks*. The main directory inside the Aimeos core is *./lib/mshoplib/setup/*, which is configured in the *manifest.php* file. Extensions can provide setup tasks in their own directories as well, as long as they are also configured in their own *manifest.php* file.

Each *setup task* can declare dependencies to other tasks, e.g. that a list of tasks must be executed before this task can run and that e.g. one task must be executed after the task completed. There will be more information about [pre- and post-dependencies](#dependencies) later as they require some more attention. The important thing during the setup process is that all tasks from all configured setup directories are sorted according to their dependencies and are executed in that order.

## Task types

1.) Those, which declare no dependencies to other tasks and are not listed as post-dependencies in other tasks. There are only a few ones because usually, each task has one or more dependencies.

2.) Next are the tasks that depend on other tasks. Maybe they want to change columns that have been changed before by other tasks. New columns that should be inserted next to columns created by other tasks are another reason. In an empty database most of these setup tasks will exit immediately because the first check is always if the necessary database table exists. Therefore, the task for creating the tables is always executed after the ones changing tables in an existing database. This reduces the time for the setup process drastically for new installations.

3.) The task for creating the tables and indexes is executed very late in the process. It reads the schema files in e.g. "./lib/mshoplib/setup/default/schema/" and executes the SQL statements if necessary.

4.) Tasks executed afterwards either need the new tables for migrating data from old ones or they will insert records into those tables. There are tasks that insert some default records e.g. for the product types. Furthermore, some tasks are executed only for specific sites: The test sites ("unittest" and "unitperf") contain their own tasks that insert or generate the required test records. One of the last tasks is usually the one for rebuilding the index for fast search operations.

Each task tests if the part of the database schema that it's written for is already up to date and prints what tables it checks. If nothing has to be done, it will only print "OK". Otherwise, it performs the necessary changes and tell you what has been done.

## Basics

The setup tasks that are part of the Aimeos core are stored in the *./lib/mshoplib/setup/* directory. Tasks only relevant for a specific site (like for unit tests or performance tests) are located in subdirectories named after the site, i.e. *./lib/mshoplib/setup/default/*,  *"*./lib/mshoplib/setup/unittest/* or  *./lib/mshoplib/setup/unitperf/*.

In the Aimeos extensions resp. your own extension, setup tasks should be in the **./lib/custom/setup/** directory or in one of the subdirectories for a specific site. You can configure the path where the setup manager is looking for tasks that should be executed within the *manifest.php* file of your extension.

```php
return [
    // ...
    'setup' => [
        'lib/custom/setup',
    ],
);
```

The "setup" key can contain a list of paths relative to the base path of the extension. The setup manager will add each task stored within these directories to the list of tasks that will be executed.

## Naming

The name of a setup task should be as specific as possible and must be unique across all extensions! The default naming scheme for tasks in the Aimeos core is:

```
<domain><action>[<subdomain>]<what>
```

Good examples are:

* IndexAddPriceTaxrateIndex
* ProductDropWarehouseEditorIndex
* CustomerAddAddressFlagsColumn
* ServiceMigrateTypeColumn

Each task should only perform one action, like adding an index or dropping an index but not both at the same time. This enables a fine grained control over the dependencies between the tasks.

!!! warning
    Never add actions of separate domains to a single task, even if they do the same! The domains can be in separate databases and much more important: This can lead to circular dependencies easily!

## Structure

The basic structure of a setup task looks like this. Please change the name of your setup task class according to the [naming schema](#naming).

```php
namespace Aimeos\MW\Setup\Task;

class TaskClassName extends \Aimeos\MW\Setup\Task\Base
{
    /**
     * Returns the list of task names which this task depends on.
     *
     * @return string[] List of task names
     */
    public function getPreDependencies()
    {
    }

    /**
     * Returns the list of task names which depends on this task.
     *
     * @return string[] List of task names
     */
    public function getPostDependencies()
    {
    }

    /**
     * Updates the schema and migrates the data
     */
    public function migrate()
    {
    }
}
```

# Managing dependencies

An essential part of setup tasks are the pre- and post-dependencies because they allow a very sophisticated ordering of the tasks. This is pretty unique across the available solutions because most of them are based on timestamps. This is OK if you have full control over your application but as soon as extensions will be able to modify the database schema too, it will break sooner or later.

The setup tasks must be executed in a specific order to work correctly. Declaring the dependencies is a more flexible way to determine this order than using numbers, dates or the alphabetic order. As existing tasks shouldn't be changed to maintain full backward compatibility, it's necessary to allow new core setup tasks to declare which tasks must run before and which ones have to be executed afterwards.

Also, extensions must be able to do the same because it wouldn't make sense for the core tasks to contain all dependencies of all existing extension tasks. The reason for extension setup tasks to be placed between core tasks is, that not only core tasks can create or update tables. If the setup task in your extension adds a column to a table it should be placed before the task which inserts the unit test data.

!!! note
    The name of the dependency is the class name, so for *Aimeos\MW\Setup\Task\TablesCreateMShop* it would be *TablesCreateMShop*. For this reason don't change the name of an existing task because then the required dependency information is lost.

!!! warning
    Only declare pre- and post-dependencies your task really depends on. Otherwise, the setup process will stop sooner or later because it can't resolve circular dependencies.

## Pre-dependencies

To find out which tasks must be executed before new ones, have a look at the SQL statements that should be executed. All tables, columns and indexes that are affected or referred by the statements should be taken into account when searching through the existing setup tasks. Most often you only have to look at the core tasks of the same domain to find all setup tasks that must be a pre-dependency to the new one.

Examples for pre-dependencies:

* *OrderAddBaseAddressAddrId* depends on *OrderRenameTables* (the comment column is added to "mshop_order_base_address" but the original name of the table was "mshop_order_address")
* *MShopAddLocaleData* depends on *TablesCreateMShop* (the languages and currencies can only inserted if the tables have been created)
* *AttributeModifyIndex* has no dependencies (dropping the index if available depends on nothing else, especially not on the existence of the table itself)

## Post-dependencies

Post-dependencies are a little bit different because you have to know what the task will do. Most often, post dependencies are used for the *TablesCreateMShop* and *CatalogRebuildIndex* or similar named tasks. The first one creates all new tables and indexes. Tasks modifying existing tables won't do anything if the tables are not yet available so adding *TablesCreateMShop* as post-dependency will speed up the process for new installations.

Examples for post-dependencies:

* *CatalogAddCode* should run before *TablesCreateMShop* (to speed up the setup process)
* *ProductAddTestData* should run before *CatalogRebuildIndex* (so the test products are written into the catalog index)

# Helper methods

As every setup task must extend the *Aimeos\MW\Setup\Task\Base* class, it inherits some methods that are required or useful to do the job. By using the base class, your task already implements the required interface *Aimeos\MW\Setup\Task\Iface*.

## Print messages

msg( '<string>', <level> )
: Prints the message indented by the given level. This method formats the messages so the output looks nice. Must be followed by a call to *$this->_status( '...' )*

status( '<string>' )
: Outputs the status for the test that was printed by *$this->_msg( ... )* before. Usual status values are: "OK" (nothing to do], "done" (task has been performed) or the number of records inserted ("<inserted>/<total>")

## Get schema/connection

getSchema( '<database domain>' )
: Retrieves the schema object for one of the databases. The parameter is one of the [[Developers/Several_databases|domains]] prefixed by "db-", e.g. "db-product"

getConnection( '<database domain>' )
: Returns the connection object for one of the databases. The parameter is the same as for *getSchema()*

## Execute SQL statements

execute( '<SQL statement>' )
: Executes a single SQL statement

executeList( <array of SQL statements> ): Executes a list of SQL statements in the order provided by the array. They are executed one by one and not inside of a transaction

getValue( '<SQL statement>', '<column name>' )
: Fetches a single record from the database and returns the value of the given column. If you need to fetch more than one record or column, use the database connection object instead

## Read platform specific SQL

getTableDefinitions( <string> )
: Extracts all table definitions from the given string (usually the content of a schema file). Each definition must be separated by two new lines ("\n")

getIndexDefinitions( <string> )
: Extracts all index definitions from the given string (usually the content of a schema file). Each definition must be separated by two new lines ("\n")

getTriggerDefinitions( <string> )
: Extracts all trigger definitions from the given string (usually the content of a schema file). Each definition must be separated by two new lines ("\n")

# Database schema

## Schema tests

tableExists( <tablename> )
: Checks if the given table name exists in the database

indexExists( <tablename>, <index name> )
: Checks if the given index (not foreign keys, primary or unique constraints) exists for the specified table in the database

constraintExists( <tablename>, <constraint name> )
: Checks if the given constraint (foreign key, primary, unique) exists for the specified table in the database

columnExists( <tablename>, <colum name> )
: Checks if the given column exists for the specified table in the database

getColumnDetails( <tablename>, <colum name> )
: Returns an object containing the details of the column implementing *Aimeos\MW\Setup\DBSchema\Column\Iface*

getDBName()
: Returns the database name

## Column details

The *getColumnDetails()* method of the schema returns an object with these methods:

getCollationType()
: Returns the collation of the column (not portable across databases)

getDataType()
: Returns the data type of the column

getDefaultValue()
: Returns the default of the column

getMaxLength()
: Returns the maximum length of the column, mainly for VARCHAR and DECIMAL columns

getName()
: Returns the name of the column

getTableName()
: Returns the name of the table the column is part of

isNullable()
: Checks if NULL values are allowed for this column

## Example code

Tests a column if NULL is allowed:

```php
$schema = $this->getSchema( 'db-product' );

if( $schema->tableExists( 'my_table' ) true
    && $schema->columnExists( 'my_table', 'my_column' ) true
    && $schema->getColumnDetails( 'my_table', 'my_column' )->isNullable() true
) {
    $this->execute( $stmt );
}
```

# Database access

## Connection methods

create( '<SQL statement>' )
: Returns a database statement object using the given SQL statement and implementing <tt>MW_DB_Statement_Interface</tt>

escape( <value> )
: Escapes the given value before it can be safely inserted into the SQL statement

begin()
: Starts a transaction for this connection

commit()
: Commits the changes done within the transaction

rollback()
: Discards the changes done inside the transaction

## Statement methods

bind( <position starting from 1>, <value>, [<type>] )
: Binds a value to a parameter in the statement. "Type" is optional and by default *Aimeos\MW\DB\Statement\Base::PARAM_STR*

execute()
: Executes the SQL statement and returns an object implementing *Aimeos\MW\DB\Result\Iface*

## Result methods

affectedRows()
: Returns the number of rows affected by a INSERT, UPDATE or DELETE statement

fetch()
: Retrieves the next row from database result set, returns false if no more rows are available

finish()
: Cleans up pending database result sets. Must be always called after retrieving all rows or executing another statement

nextResult()
: Retrieves next database result set if the SQL statement contained multiple statements

## Example code

```php
$conn = $this->getConnection( 'db-product' );

$stmt = $conn->create( 'SELECT * FROM my_table WHERE type = ?' );
$stmt->bind( 1, 'payment' );
$result = $stmt->execute();

while( ( $row = $result->fetch() ) !# false ) {
    // process row
}

$result->finish();
```
