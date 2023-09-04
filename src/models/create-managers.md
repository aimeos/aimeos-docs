# Extend existing domain

## Database setup

If you want to add a table for your manager to an existing data domain, then read the article about [adding new tables](../infrastructure/schema-migrations.md#add-new-tables).

For example, let's add a table to the **product** domain named *mshop_product_test*. Create a new `./<yourext>/setup/default/schema/product.php` file to your extension that creates the *mshop_product_test* table:

```php
return array(
    'table' => array(
        'mshop_product_test' => function ( \Aimeos\Upscheme\Schema\Table $table ) {
            $table->engine = 'InnoDB';

            $table->id()->primary( 'pk_msprote_id' );
            $table->string( 'siteid' );
            $table->string( 'label' )->default( '' );
            $table->int( 'pos' )->default( 0 );
            $table->smallint( 'status' )->default( 1 );
            $table->meta();

            $table->index( ['status', 'siteid', 'pos'], 'idx_msprote_status_sid_pos' );
            $table->index( ['label', 'siteid'], 'idx_msprote_label_sid' );
        },
    ),
);
```

!!! note
    All columns beside *id* and *siteid* must have a default value!

To create the new table in the database, you have to execute the setup tasks:

Laravel
: **php artisan aimeos:setup**

TYPO3
: **php vendor/bin/typo3 aimeos:setup** (or via the update script in the extension manager)
