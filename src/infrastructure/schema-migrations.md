In Aimeos, setup tasks are responsible for creating the database schema, updating the schema if necessary and migrating data required due to schema changes. They have to perform their tasks for all supported databases and [Upscheme](https://upscheme.org) provides the necessary infrastructure for that.

The setup tasks have a lot of advantages and exceed the possibilities of other available solutions like ["Object-relational mapping" (ORM)](https://en.wikipedia.org/wiki/Object-relational_mapping) or similar alternatives to setup tasks:

* The database structure is stored in the version control system
* For every commit there can be a suitable database structure created
* Everyone can update their existing database to a newer version
* Updates are possible from any commit, not only from released versions
* Data transformation is possible via PHP code if SQL is not enough
* They can declare dependencies to other tasks

They are also used to write the default and unit test data to the database during the setup process.

# Schema updates

Updating an existing schema or adding a new table to an existing data domain (product, catalog, attribute, etc.) by using [Upscheme](https://upscheme.org) is very simple and described here. If you need to migrate data, want to add a new data domain or rename a table, you need to create your own [setup task](#migration).

For already existing data domains, a schema file exists in the [./setup/default/schema/](https://github.com/aimeos/aimeos-core/tree/master/setup/default/schema) directory of the Aimeos core. It consists of the list of tables including their definitions. The *attribute.php* file contains these lines for example:

```php
return [
  'table' => [
    'mshop_attribute_type' => function ( \Aimeos\Upscheme\Schema\Table $table ) {

        $table->id()->primary();
        $table->string( 'siteid' );
        $table->string( 'domain', 32 );
        $table->code();
        $table->string( 'label' );
        $table->smallint( 'status' );
        $table->meta();

        $table->unique( ['siteid', 'domain', 'code'], 'unq_msattty_sid_dom_code' );
        $table->index( ['siteid', 'status'], 'idx_msattty_sid_status' );
        $table->index( ['siteid', 'label'], 'idx_msattty_sid_label' );
        $table->index( ['siteid', 'code'], 'idx_msattty_sid_code' );
    },

    // ...
  ],
],
```

An anonymous function creates the table and adds the columns as well as the indexes. An important detail is to return the updated schema. This object will then be passed to the anonymous function for the same table in your extension.

!!! warning
    Please remember that identifiers (table/column/index names) must **not be longer then 30 characters**!

## Add new tables

In your own extension you have to create a PHP file with the same name as the file for the existing data domain, i.e. *attribute.php* in the *./setup/default/schema/* directory. This file can contain one or more anonymous functions for new tables of the same data domain. They are created by [Upscheme](https://upscheme.org) exactly like in the Aimeos core, e.g.

```php
return [
  'table' => [
    'mshop_attribute_mytable' => function ( \Aimeos\Upscheme\Schema\Table $table ) {

        $table->id()->primary( 'pk_msattmy_id' );
        $table->string( 'siteid' );
        $table->string( 'myvalue', 'string' )->null( true );
        $table->meta();

        $table->unique( ['siteid', 'myvalue'], 'unq_msattmy_sid_myval' );
    },
  ],
];
```

## Modify existing tables

It's possible to modify schema definitions of core tables via extensions. This enables your extension to add additional columns or indexes to core tables or change column options like their length or type. Your changes will be applied to the tables while the setup tasks are running as long as your extension is installed.

You have to create a PHP file with the same name as the file for the existing data domain, i.e. *attribute.php* in the *./setup/default/schema/* directory - just like for adding a new table.

The important difference compared to adding new tables is that the schema object already contains a table definition. The current table definition is passed to your function and you can use all methods offered by [Upscheme](https://upscheme.org) to modify or add columns/indexes/etc., e.g.:

```php
return [
  'table' => [
    'mshop_attribute_type' => function ( \Aimeos\Upscheme\Schema\Table $table ) {

        $table->string(  'domain', 64] );
        $table->int( 'pos' )->default( 0 );

        $table->index( ['code', 'pos'],'idx_msattty_code_pos' );
    },
  ],
];
```

## Tables for new domains

In order to create tables for a new data domain (not existing ones like "attribute", "product", "service", etc.], you need to create an [Upscheme](https://upscheme.org) setup task, too. This setup task must extend from the `Base` setup task class. For a new domain *mydomain* (defined in *./setup/default/schema/mydomain.php*) create a file called *Mydomain.php* with content similar to this one:

```php
namespace Aimeos\Upscheme\Task;

class Mydomain extends Base
{
    public function up()
    {
        $this->info( 'Creating mydomain schema', 'v' );
        $db = $this->db( 'db-mydomain' );

        foreach( $this->paths( 'default/schema/mydomain.php' ) as $filepath )
        {
            if( ( $list = include( $filepath ) ) === false ) {
                throw new \RuntimeException( sprintf( 'Unable to get schema from file "%1$s"', $filepath ) );
            }

            foreach( $list['table'] ?? [] as $name => $fcn ) {
                $db->table( $name, $fcn );
            }
        }
    }
}
```

In the *up()* method, you need to get the connection to the database where the table(s) should be created in using *$this->db('db-mydomain')*. If no connection for *db-mydomain* is configured, it will automatically fall back to the default connection.

The file *default/schema/mydomain.php* contains your schema definition and the path must be relative to the *./setup* directory of your extension.

Finally, the functions retrieved from the schema file(s) will be passed to the *$db->table()* method which will create the table definitions according to the schema file.

## Platform specific

Sometimes you might need to use column or index options that are only available for specific database servers, e.g. a MySQL fulltext index. [Upscheme](https://upscheme.org) allows passing the database type as third argument to the [opt()](https://upscheme.org/#columnopt) method so the option will be only used if the database matches the given type.

```php
return [
  'table' => [
    'mshop_attribute_type' => function ( \Aimeos\Upscheme\Schema\Table $table ) {
        $table->string( 'code', 64] )->opt( 'unique', true, 'mssql' );
    },
  ],
];
```

Also, the [Upscheme database](https://upscheme.org#database) schema object offers a [for()](https://upscheme.org#dbfor) method to execute custom SQL statements only for the passed database type:

```php
public function up()
{
    $this->db( 'db-index' )->for( 'mysql', 'CREATE FULLTEXT INDEX `idx_msindte_content` ON `mshop_index_text` (`content`)' );
}
```

# Migrations

The following section describes how setup tasks can migrate data before or after the schema updates are done.

## Basics

Migration tasks are setup tasks like the ones creating the database schema and stored in the **./setup/** directory but instead of defining a table structure, they migrate the data in the existing tables to fit to the new schema. Tasks only relevant for a specific site (like for unit tests or performance tests) are located in sub-directories named after the site, i.e.

* ./setup/default/
* ./setup/unittest/
* ./setup/unitperf/

You can change the path, where the setup process looks for tasks to execute, within the *manifest.php* file of your extension. The default directory is:

```php
return [
    // ...
    'setup' => [
        'setup',
    ],
];
```

The "setup" key can contain a list of paths relative to the base path of the extension. The setup manager will add each task stored within these directories to the list of tasks that will be executed.

## Naming

The name of a setup task should be as specific as possible and must be **unique across all extensions**! The default naming scheme for tasks in the Aimeos core is:

```
<domain><action>[<subdomain>]<what>
```

Good examples are:

* IndexAddPriceTaxrateIndex
* ProductDropWarehouseEditorIndex
* CustomerAddAddressFlagsColumn
* ServiceMigrateTypeColumn

!!! warning
    Don't add actions of separate domains to a single task, even if they do the same! The domains can be in separate databases and much more important: This can lead to circular dependencies easily!

## Structure

The basic structure of a setup task looks like this (please change the name of your setup task class according to the [naming schema](#naming)):

```php
namespace Aimeos\Upscheme\Task;

class TaskClassName extends Base
{
	/**
	 * This task will run after the returned list of task names
	 *
	 * @return array<string> List of task names
	 */
	public function after() : array
	{
		return [];
	}

	/**
	 * This task will run before the returned list of task names
	 *
	 * @return array<string> List of task names
	 */
	public function before() : array
	{
		return [];
	}

    /**
     * Updates the schema and migrates the data
     */
    public function up()
    {
        $this->info( 'Migrating ...', 'v' );
        // ...
    }
}
```

The *after()* and *before()* methods are optional and only necessary if you need to define dependencies to other tasks.

# Dependencies

The *after()* and *before()* methods are crucial for executing setup tasks, because they allow a very sophisticated ordering of these tasks. Let's take this task as example:

```php
namespace Aimeos\Upscheme\Task;

class TaskClassName extends Base
{
	public function after() : array
	{
		return ['Product'];
	}

	public function before() : array
	{
		return ['MShopSetLocale'];
	}

    public function up()
    {
        $this->info( 'Adding GTIN product column', 'v' );

        $this->db( 'db-product' )->table( 'mshop_product', function( $table ) {
            $table->string( 'gtin', 36 )->default( '' );
            $table->index( ['siteid', 'gtin'] );
        } );
    }
}
```

Due to the values returned by the *after()* and *before()* methods, the *up()* method of this task will be executed between the *Product* and the *MShopSetLocale* task. Thus, we can be sure the table definition for the product table is already available but e.g. no unit test data is added yet (besides the records that are already there).

The name of the dependency is the class name, so for *Aimeos\Upscheme\Task\Product* it would be *Product*. For this reason don't change the name of an existing task because then the required dependency information is lost.

!!! warning
    Only declare before/after dependencies your task really depends on. Otherwise the setup process will stop sooner or later because it can't resolve circular dependencies.
