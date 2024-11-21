Usually, it's only rarely necessary to extend existing managers and items because most of the data can be associated to items via the list tables. The data can then be stored as attributes, texts or properties (in case of product items) instead.

To extend or overwrite existing classes, you have to:

* Extend the database table (refer to [schema updates](../infrastructure/schema-migrations.md))
* Create a new class in your project specific Aimeos extension
* Store the class file in the `./src/` directory
* Use the same directory structure as for the original class below the `./src/` directory, e.g. `./src/MShop/Product/Manager/`
* Give it a different name as the original class, e.g. *Myproject*
* Extend from the original class

# Database setup

If you need to store e.g. an arbitrary value of another system in your product table, you can [extend the existing table](../infrastructure/schema-migrations.md) by adding a new field like described in the article about modifying existing tables.

Let's name the new field "mycolumn". Add a new `./<yourext>/setup/default/schema/product.php` file to your extension that adds your new column to the *mshop_product* table:

```php
return array(
  'table' => array(
    'mshop_product' => function ( \Aimeos\Upscheme\Schema\Table $table ) {
        $table->string( 'mycolumn', 32 )->null( true );
    },
  ),
);
```

!!! note
    The new column must be nullable, that means it must allow NULL values!

To create the new column in the database, you have to execute the setup tasks:

Laravel
: **php artisan aimeos:setup**

TYPO3
: **php vendor/bin/typo3 aimeos:setup** (or via the update script in the extension manager)

# Easy way

Since 2019.10 it's possible to add new columns by extending the database table and a manager decorator only. The example will use the product manager but you can extend all managers in the same way.

Implementing decorators is a great way to dynamically extend managers without inheriting from the existing manager class. Instead, you can wrap multiple decorators around a manager object like the layers of an onion. In each decorator, you can implement additional code that changes the parameters or the result of the manager method or performs additional actions.

## Manager decorator

You need to create a decorator for the product manager that will care about the new column(s). A decorator has the advantage that you can add multiple decorators on top of the manager and 3rd party extensions can do that too.

Your new product manager decorator class should be located in `./<yourext>/src/MShop/Product/Manager/Decorator/Myproject.php` and should contain:

```php
namespace Aimeos\MShop\Product\Manager\Decorator;

class Myproject extends \Aimeos\MShop\Common\Manager\Decorator\Base
{
    private $attr = [
        'product.mycolumn' => [
            'internalcode' => 'mycolumn',
            'label' => 'My new column',
            'type' => 'string', // optional
        ],
    ];

    public function getSaveAttributes() : array
    {
        return parent::getSaveAttributes() + $this->createAttributes( $this->attr );
    }

    // optional, only required for adding search functions
    public function getSearchAttributes( bool $sub = true ) : array
    {
        return parent::getSearchAttributes( $sub ) + $this->createAttributes( [
            // ...
        ] );
    }
}
```

The `$attr` array contains a definition of the column(s) and the requirements are:

* The key must be exactly the name of your column in the database (here: 'mycolumn')
* The value for *internalcode* must be SQL alias of the table, a dot and the column name enclosed in quotation marks (here: 'mpro."mycolumn"')

!!! tip
    For the SQL alias you have to use, please have a at into the SELECT statement of the domain in the [configuration](https://github.com/aimeos/aimeos-core/tree/master/config/mshop).

The other values in the *$attr* array are optional:

* *label* is an arbitrary string that is shown in admin interface in the search bar
* *type* is the type of the values that the column contains (default: 'string') and can be:
    * bool
    * date
    * datetime
    * decimal
    * float
    * int
    * json
    * string

As last step, you have to add your decorator name to the list of local decorators for that manager in the `./<yourext>/config/mshop.php` file. For the product manager it's:

```php
return [
    'product' => [
        'manager' => [
            'decorators' => [
                'local' => ['Myproject']
            ]
        ]
    ]
];
```

## Item properties

Afterwards, you can access the values of your new columns in the item using:

```php
$item->get( 'product.mycolumn', '<default value>' );
```

You can also register new methods in each item class which transforms the values to enforcing types for example:

```php
\Aimeos\MShop\Product\Item\Standard::macro( 'getMycolumn', function() {
    return (int) $this->get( 'product.mycolumn' );
} );

\Aimeos\MShop\Product\Item\Standard::macro( 'setMycolumn', function( $value ) {
    return $this->set( 'product.mycolumn', (int) $value );
} );
```

It's also possible to add new methods that combine several values like:

```php
\Aimeos\MShop\Customer\Item\Standard::macro( 'getCombined', function() {
    return $this->get( 'product.code' ) . '-' . $this->get( 'product.mycolumn' );
} );
```


# Custom way

To have full control over the implementation including those of the item, you need to do a bit more.

## Items

The skeleton for your new product item class would be located in `./<yourext>/src/MShop/Product/Item/Myproject.php` and should contain:

```php
namespace Aimeos\MShop\Product\Item;

class Myproject extends Standard
{
    public function getMyColumn() : string
    {
        return $this->get( 'product.mycolumn', '' );
    }

    public function setMyColumn( ?string $val ) : \Aimeos\MShop\Product\Item\Iface
    {
        return $this->set( 'product.mycolumn', $val );
    }

    public function fromArray( array &$list, bool $private = false ) : \Aimeos\MShop\Product\Item\Iface
    {
		$item = parent::fromArray( $list, $private );

		foreach( $list as $key => $value )
		{
			switch( $key )
			{
                case 'product.mycolumn': $item = $item->setMyId( $value ); break;
				default: continue 2;
            }
			unset( $list[$key] );
        }

        return $item;
    }

	public function toArray( bool $private = false ) : array
    {
        $list = parent::toArray( $private );

        if( $private === true ) {
            $list['product.mycolumn'] = $this->getMyId();
        }

        return $list;
    }
}
```

The *fromArray()* and *toArray()* methods are important if you need to manage your new properties via the admin interface. By using calls of the parent class you can use the existing code and only add new code for your own property.

## Managers

Your new product manager class should be stored in `./<yourext>/src/MShop/Product/Manager/Myproject.php` and usually contains:

```php
namespace Aimeos\MShop\Product\Manager;

class Myproject extends Standard
{
    private $searchConfig = [
        'product.mycolumn' => [
            'internalcode' => 'mycolumn',
            'label' => 'Product additional column',
            'type' => 'string', // int, float, etc.
        ],
    ];

    public function save( $items, bool $fetch = true )
    {
        foreach( map( $items ) as $item ) {
            // a modified copy of the code from the parent class
            // extended by an additional bind() call
		}
        return $items;
    }

    public function getSearchAttributes( bool $withsub = true ) : array
    {
        return parent::getSearchAttributes( $withsub ) + $this->createAttributes( $this->attr );
    }

	protected function createItemBase( array $values = [], array $listItems = [],
		array $refItems = [], array $propertyItems = [] ) : \Aimeos\MShop\Common\Item\Iface
    {
        return new \Aimeos\MShop\Product\Item\Myproject( $values, $listItems, $refItems, $propertyItems );
    }
}
```

The `$searchConfig` and `getSearchAttributes()` method will allow you to use the defined code (`product.myvalue`) in search criteria expressions passed to `search()`.

You also need to add a new SQL SELECT statement to the configuration, so the values are fetched from the database.

## Search functions

It's not possible to e.g. use a column name as argument for conditions, only fixed values. This would be only possible in SQL but e.g. not in other storages like ElasticSearch. To support all type of storages, you have to add a "search function" like in the [product manager](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Product/Manager/Standard.php).

It can contain storage (SQL) specific code and to compare two columns in the `mshop_product` table for example you need to add this to your custom manager:

```php
'product:check' => [
	'code' => 'product:check()',
	'internalcode' => '(mpro."start" < mpro."end)"',
	'label' => 'Checks valid start/end dates',
	'type' => 'boolean',
	'internaltype' => 'boolean',
	'public' => false,
],
```

Then, you can add this condition by using:

```php
$filter->add( $filter->make( 'product:check', [] ), '==', true )
```

This will create a MySQL query like:

```sql
SELECT * FROM mshop_product WHERE (mpro."start" < mpro."end") = 1
```

And in PostgreSQL it will be:

```sql
SELECT * FROM mshop_product WHERE (mpro."start" < mpro."end") = true
```

Because the expression in `internalcode` is always compared to some value, it must return something that is comparable to a value or NULL. In this case it's a boolean true/false value but in other cases, you need to add a subquery in `internalcode` to match that need and compare against a (not) NULL value.

There's also more information available about [how to use search functions](search-filter.md#search-functions).

## Testing

All test class must be in the `./<yourext>/tests/` directory using the same directory structure as in `./src/`, e.g. `./<yourext>/tests/MShop/Product/Item/MyprojectTest.php` the `...Test.php` extension is important so PHPUnit will recognize these files as test classes. For items, they usually consist of

```php
namespace Aimeos\MShop\Product\Item;

class MyprojectTest extends \PHPUnit\Framework\TestCase
{
    private $object;

    protected function setUp() : void
    {
        $values = ['myvalue' => 'test'];
        $this->object = new \Aimeos\MShop\Product\Item\Myproject( $values );
    }

    public function testGetMyColumn()
    {
        $this->assertEquals( 'test', $this->object->getMyColumn() );
    }

    public function testSetMyolumn()
    {
        $this->object->setMyColumn( 'test2' );
        $this->assertEquals( 'test2', $this->object->getMyColumn() );
        $this->assertTrue( $this->object->isModified() );
    }

    public function testFromArray()
    {
        $this->object->fromArray( ['product.myvalue' => '123'] );
        $this->assertEquals( '123', $this->object->getMyColumn() );
    }

    public function testToArray()
    {
        $list = $this->object->toArray();
        $this->assertEquals( 'test', $list['product.myvalue'] );
    }
}
```

For your new manager, you should also test the methods you've implemented:

```php
namespace Aimeos\MShop\Product\Manager;

class MyprojectTest extends \PHPUnit\Framework\TestCase
{
    private $object;

    protected function setUp() : void
    {
        $context = \TestHelperMShop::context();
        $this->object = new \Aimeos\MShop\Product\Manager\Standard( $context );
    }

    public function testSaveItem()
    {
        // modified test method of the "StandardTest" class with your new property
    }

    public function testGetSearchAttributes()
    {
        $list = $this->object->getSearchAttributes();
        $this->assertArrayHasKey( 'product.mycolumn', $list );
    }
}
```

To test your extension, you have to

* checkout the [Aimeos core](https://github.com/aimeos/aimeos-core) in a separate directory
* run **composer update** to install the required dependencies
* configure your database in `./config/resources.php`
* store your new extension in the `./ext/` sub-directory e.g. as `./ext/me-myproject/`
* execute **./vendor/bin/phing setup** to create the tables and add the unittest data
* execute **./vendor/bin/phing -Ddir=ext/me-myproject testext** to run your tests
