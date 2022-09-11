The `search()` method of each manager accepts a filter as first argument. You can create the filter object with:

```php
$filter = $manager->filter();
$filter = $manager->filter( true );
```

The second example using *true* as first argument automatically adds the default conditions to the filter, i.e. the manager will only return items which are enabled and can be shown in the frontend.

# Compare

A criterion consists of three parts:

* search key
* operator
* value

You can set a new criterion using:

```php
$filter->add( 'product.code', '==', 'test' );
```

Available operators are:

* **==** (equals)
* **!=** (not equals)
* **<** (less than)
* **<=** (less than or equal)
* **>** (greater than)
* **>=** (greater than or equal)
* **=~** (string starts with)
* **~=** (string contains, slow!)

The available search keys depend on the used manager and the item properties. Each manager defines its search keys in its class like the [product manager](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Product/Manager/Standard.php#L30). If the list of search keys depend on the implementation or is dynamic, you can retrieve the available search keys by using *getSearchAttribute()*.

Values for criteria can be more than single values. You can hand over a list of values as well:

```php
$filter->add( 'product.id', '==', [1, 5, 7] );
```

It's also possible to specify several criteria as condition to filter the returned items according to them:

```php
$filter->add( [
    'product.id' => [1, 5, 7],
    'product.code' => 'test'
] );
```

These conditions would search for a product item with "test" as code and the product IDs "1", "5", or "7". The default operator is "==" in that case. If you need a different operator for all conditions, you can use:

```php
$filter->add( [
    'product.id' => 10,
    'product.status' => 0
], '>' );
```

Then, all product items with ID greater than 10 and status greater than 0 will be returned.

# Combine

You can combine a list of conditions in several ways:

* **and()** (AND combination)
* **or()** (OR combination)
* **not()** (NOT, only for single conditions)

```php
$filter->add( $filter->and( [
    $filter->or( [
        $filter->is( 'product.datestart', '<', '2000-01-01' ),
        $filter->is( 'product.datestart', '==', null ),
    ] ),
    $filter->or( [
        $filter->is( 'product.dateend', '>', '2000-01-01' ),
        $filter->is( 'product.dateend', '==', null ),
    ] ),
] );
```

In the example the additional *is()* method is used, which is almost the same as *add()* but it doesn't add the condition to the filter object. Instead, it returns the condition so it can be used for *and()*, *or()* and *not()*.

The *not()* method is special in this case because its only valid for single conditions. But you can use the *and()* or *or()* methods to combine several conditions to one before using *not()*:

```php
$filter->add( $filter->not( $filter->is( 'product.status', '==', 0 );

// or combine several conditions and negate them:
$filter->add( $filter->not( $filter->and( [
    $filter->is( 'product.type', 'default' ),
    $filter->is( 'product.status', 0 ),
] ) ) );
```

# Search functions

There's one further type of conditions named "search functions". They offer complex queries for searching items by a syntax which is easier to use - just like PHP functions hiding complex tasks.

You can identify a search function by the round parenthesis at the end of their code, e.g. "product:has()" offered by the managers supporting lists of references. Search functions need one or more parameter which are described in the label of the criteria attribute.

If you want to search for items that has referenced data via the list table or properties, there are two search functions *:has* and *:prop* available for each domain, i.e for the product domains their names are *product:has* and product:prop*:

* :has : `[<domain>, <list type>, <referenced ID>]`
* :prop : `[<property type>, <language ID>, <property value>]`

The second and the third array element (<list type> and <referenced ID> as well as <language ID> and <property value>) are optional.

```php
$filter->add( 'product.type.code', '==', 'select' )
    ->add( $filter->make( 'product:has', ['attribute', 'default', 123] ), '!=', null )
    ->add( $filter->make( 'product:prop', ['ISBN', null, 'abc'] ), '!=', null );
```

These criteria would return all product items that are selection products, having a referenced attribute with list type "default" and attribute ID "123" as well as a property of type "ISBN", which isn't language specific and equals "abc".

!!! warning
    The PHP type of the parameters used in the second argument must be exactly as expected, e.g. if an integer value is required, passing a float value may fail or lead to strange behavior.

# Sorting

Each search key can be used for sorting the result set:

```php
$filter->order( 'product.id' ),
$filter->order( '-product.id' ),
```

The first character of the sort key can be "+", "-" or none to indicate the direction of the sorting. Available values are:

* **+ or none** (plus for ascending order)
* **-** (minus for descending order)

Several search keys at once are allowed too:

```php
$filter->order( ['product.status', '-product.id'] ),
```

The result set is ordered by the product status first and if two or more items have the same status, they are ordered by their ID in descending order in that example.

!!! warning
    Please make sure an appropriate index is available before using the search key for sorting the result. Otherwise, retrieving the items will be extremely slow!

# Paging

If your shop contains more than a few items, paging comes into play. By default, only the first 100 found items will be returned by `search()`. To retrieve items beyond or with a different slice size, you should use the *slice()* method of the search object:

```php
$filter->slice( 100, 50  );
```

The first argument is the starting point, the second one the slice size when fetching items. The parameters in the example would retrieve the product items sorted by their ID from position 100 to 150.

You can get the start value and the number of returned items if you need them using:

```php
$start = $filter->getOffset();
$num = $filter->getLimit();
```

# Debugging

If you want to know which conditions have been added to the filter, you can use the *__toArray()* method:

```php
print_r( $filter->__toArray() );
```

This will print all (nested) conditions of the filter that will be used by the manager if you pass the filter to the `search()` method of the manager.

# Fetch records efficiently

Retrieving records in the database is always done in bunches (default: 100 records/search, can be changed using `slice()`) and if you need to process more or all items, you have to repeatedly call `search()` of the manager. The most efficient code for this is:

```php
$manager = \Aimeos\MShop::create( $this->context(), 'product' );
$filter = $manager->filter()->order( 'product.id' );

while( !( $items = $manager->search( ( clone $filter )->add( 'product.id', '>', $lastId ?? 0 ), ['text'] ) )->isEmpty() )
{
    foreach ( $items as $item ) {
        // process items
    }

    $lastId = $items->last()->getId();
}
```

Some managers (e.g. index and product managers) are implementing the `iterator()` and `iterate()` methods which should be used if you need to fetch all records subsequently:

```php
$manager = \Aimeos\MShop::create( $this->context(), 'product' );
$iterator = $manager->iterator( $manager->filter() );

while( $items = $manager->iterate( $iterator, ['text'], 100 ) )
{
    foreach ( $items as $item ) {
        // process items
    }
}
```
