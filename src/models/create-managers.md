# Database setup

## Extend existing domain

If you want to add a table for your manager to an existing data domain, then read the article about [adding new tables](../infrastructure/schema-migrations.md#add-new-tables).

For example, let's add a table to the **product** domain named *mshop_product_test*. Create a new `./<yourext>/setup/default/schema/product.php` file to your extension that creates the *mshop_product_test* table:

```php
return array(
    'table' => array(
        'mshop_product_test' => function ( \Aimeos\Upscheme\Schema\Table $table ) {
            $table->engine = 'InnoDB';

            $table->id()->primary( 'pk_msprote_id' );
            $table->int( 'parentid' );
            $table->string( 'siteid' );
            $table->string( 'label' )->default( '' );
            $table->int( 'position' )->default( 0 );
            $table->smallint( 'status' )->default( 1 );
            $table->meta();

            $table->index( ['status', 'siteid', 'position'], 'idx_msprote_status_sid_pos' );
            $table->index( ['label', 'siteid'], 'idx_msprote_label_sid' );

			$table->foreign( 'parentid', 'mshop_product', 'id', 'fk_msprote_pid' );
        },
    ),
);
```

!!! note
    All columns beside *id* and *siteid* must have a default value if they are not required explicitely like *parentid*!

!!! tip
    For more information about the available database schema methods, have a look into the documentation of the [Upscheme](https:://upscheme.org) project.

To create the new table in the database, you have to execute the setup tasks:

Laravel
: **php artisan aimeos:setup**

TYPO3
: **php vendor/bin/typo3 aimeos:setup** (or via the update script in the extension manager)

# Create manager

## Existing domain

After the table has been created, you can implement the corresponding manager. Create a new file named `./<yourext>/src/MShop/Product/Manager/Test/Standard.php` with a class like this one:

```php
namespace Aimeos\MShop\Product\Manager\Test;

class Standard
	extends \Aimeos\MShop\Common\Manager\Base
	implements \Aimeos\MShop\Common\Manager\Iface
{
	public function getSaveAttributes() : array
	{
		return $this->createAttributes( [
			'parentid' => [
				'type' => 'int',
				'public' => false
			],
			'label' => [
			],
			'status' => [
				'type' => 'int',
			],
			'position' => [
				'type' => 'int',
				'label' => 'Position for sorting'
			],
		] );
	}
```

You must name the class *Standard.php* because it's the name the factories will use by default. Otherwise, you need to set the name of the manager using the *mshop/product/manager/test/name* configuration. Also extend your class from the *\Aimeos\MShop\Common\Manager\Base* class and implement the *\Aimeos\MShop\Common\Manager\Iface*!

By default, you only have to implement the *getSaveAttributes()* method which must return the list of properties that can be managed by the class and stored in the corresponding table. The *id*, *siteid*, *ctime*, *mtime* and *editor* properties are added by default.

The array must contain the column name as key, all properties in the array assigned to the key are optional and the **default type** of the column is assumed to be **string**. Available array properties for each key are:

* *label* : Label used in the search box of the admin backend
* *public* : Property is shown in the admin backend and assigned in the *fromArray()* method of the item
* *internalcode* : String that will be used instead of the key name as column name
* *type* : Type of the database column which can be:
    * bool
    * date
    * datetime
    * decimal
    * float
    * int
    * json
    * string

If one of your column names is a reserved word in the database, you must put the column name into quotes, e.g.:

```php
'key' => [
    'internalcode' => '"key"',
],
```

If you need a different table name, implement the *getTable()* method to return your custom table name:

```php
protected function getTable() : string
{
    return 'myapp_test';
}
```

Afterwards, you can create your new manager using the MShop factory and use all methods provided by managers like *create()*, *cursor()*, *delete()*, *filter()*, *get()*, *iterate()*, *save()* and *search()*. If you need *aggregate()* and *find()*, you have to implement them in your manager class because there are no default implmentations available.