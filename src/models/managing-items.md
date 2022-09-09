In *Aimeos*, all data like products, categories, texts, prices, attributes, etc. is managed by a persistence layer located in the *./src/* directory of the *Aimeos* core.

Using managers and items which offer a common interface to the stored data allows accessing the data regardless of where and how it is stored. Thus, it doesn't matter if all data or parts of it is stored in a relational or document-oriented database, if it can be accessed via SQL or with a different query language.

# Data domains

Each kind of data is stored in one "domain", a term defined by the [domain driven design](https://en.wikipedia.org/wiki/Domain-driven_design) method. A domain contains the data and code for a common context, like the catalog domain which consists of categories and related data including the managers which know how to store, manipulate and retrieve those data.

These domains are part of the *Aimeos* core:

* attribute (shared attributes between entries)
* cache (temporary cached content)
* catalog (category tree and associated data)
* coupon (reductions and vouchers)
* customer (customer data and addresses)
* index (product index for fast lookup)
* job (jobs created by the admin interface)
* locale (sites, languages and currencies)
* log (message logging)
* media (images, files, documents)
* order (orders created by customers)
* plugin (event-driven basket changes)
* price (for items of other domains)
* product (basic product and related data)
* review (customer reviews)
* rule (price rules)
* service (delivery and payment options)
* stock (product stock levels)
* subscription (repeating customer subscriptions)
* supplier (information about product suppliers)
* tag (arbitrary tagging of items)
* text (for items of other domains)

# Items

Data from a domain is stored in one or more items, objects mainly, with *getter* and *setter* methods but without much own logic. They are container for transferring data between layers, e.g to the clients or from the controllers back to the storage.

The available properties of each item class depend on the domain and are different for each item. A few properties are part of all domains which include:

* id (Unique ID of the entry)
* siteid (for multi-tenancy support)
* ctime (creation date/time)
* mtime (modification date/time)
* editor (last editor of the entry)

For more information, please have a look into the available *getter* and *setter* methods for the domain items you are looking for, e.g. the [product item](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Product/Item/Standard.php).

# Managers

There's exactly one manager for each item type, so a product item has its own manager as well as a product property item has its own one. All managers know how to create, store, retrieve and delete "their" items and only theirs. They don't care about items of other domains or of sub-managers of their domain.

If you need a shop related manager to fetch or store items, you can use the factory class to get an instance of the manager:

```php
$manager = \Aimeos\MShop::create( $context, 'catalog' );
$manager = \Aimeos\MShop::create( $context, 'product' );
$manager = \Aimeos\MShop::create( $context, 'service' );
```

The second argument is the path of the manager. The same principle applies to the other domains as well. For the admin related managers use:

```php
$manager = \Aimeos\MAdmin::create( $context, 'job' );
$manager = \Aimeos\MAdmin::create( $context, 'log' );
$manager = \Aimeos\MAdmin::create( $context, 'cache' );
```

The necessary context object is available in all controllers and clients via `$this->context()`, but this doesn't apply to views!

!!! note
    The "cache" and "log" managers are only necessary to have full access to their items. If you only want to [log](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/ContextIface.php#L147) messages or [cache](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/ContextIface.php#L25) some content, you should use the objects from the context instead!

# Manager methods

## Create item

Creating a new empty item is the easiest part. Simply call the `create()` method of the manager you need a new item from:

```php
$item = $manager->create();
$item = $manager->create( [/*...*/] );
```

This creates a new object with some default values for the item set. You can add properties if you pass a list of key/value pairs:

```php
$item => $manager->create( ['domain.key1' => 'value1', 'domain.key2' => 'value2'] )
// Example for a product item:
$item => $manager->create( ['product.code' => 'test', 'product.label' => 'Test'] )
```

To find out more which keys are available for the items of the domain, use `toArray()`:

```php
$item->create()->toArray()
```

The item isn't stored in the database and doesn't have an unique ID yet.

!!! note
    If you add item properties as first argument, the state of the item is *not modified*! Passing it to `save()` won't persist the item in the database until you call `$item->setModified()` too.

!!! warning
    Don't create an item (like every other object) with the "new" operator! Depending on the implementation of the manager, different items implementing the same interface can be returned.

## Save item

After you've filled the item with data, you can ask the manager to persist it in the storage with a call to the `save()` method:

```php
$item = $manager->save( $item );
$items = $manager->save( $items );
```

The manager will try to store the data, retrieve the unique ID for the item and update the ID property of the item. The parameter must be an item object returned by `create()` of the same manager. Passing an item object from another manager will throw an exception.

!!! tip
    There's a second parameter available which can be used to optimize performance if you don't need the unique ID afterwards. If you pass ''false'' as second parameter, the ID property won't be updated.

## Get item

You can retrieve a single item if you know its unique ID. The `get()` method returns exactly one item, if the manager found one for the given ID, or throws an exception, if none is found:

```php
$item = $manager->get( $id );
$item = $manager->get( $id, ['text', 'media', 'price'] );
$item = $manager->get( $id, ['attribute' => ['default', 'variant']] );
$item = $manager->get( $id, ['supplier' => ['text', 'media']] );
```

There's an optional second parameter to fetch items from associated domains too. It can be either a list of domains:

```php
['text', 'media', 'price']
```

which will fetch all items of the "text", "media" and "price" domains. You can also pass the domain name as key and the list types as values:

```php
['attribute' => ['default', 'variant']]
```

to fetch only attributes which are associated to the item with "default" or "variant" list types. For some managers like the product manager it's also possible to fetch categories, suppliers an stock items.

For the *catalog* and *supplier* items you can declare which referenced items should be retrieved. They are available for all domain items where items from other domains can be associated to them via a "list" table.

```php
['supplier' => ['text', 'media']]
```

which will add the supplier(s) of a product including their "text" and "media" items.

Domains with a list table where related items can be referenced are:

* attribute
* catalog
* customer
* media
* price
* product
* service
* supplier
* text

Items from each domain passed in the second argument will be part of the returned item. You can access these associated items via the *getListItems()* and *getRefItems()* methods, e.g.

```php
$textref = $item->getListItems( 'text', 'default', 'name', true );
$texts = $item->getRefItems( 'text', 'name', 'default', true );
```

The second parameter for *getListItems()* and the third parameter for *getRefItems()* define the type of association between the domain items. When the fourth parameter is false, all items are retured even if they shouldn't be available in the frontend. All parameters of both methods are optional.

You can also retrieve items stored in the same domain, e.g. product properties or ordered products, via the second parameter:

```php
$item = $productManager->get( $id, ['product/property'] );
$item = $orderBaseManager->get( $id, ['order/base/address', 'order/base/product'] );
```

## Find item

Single items which can be identified by their code or a combination of the code, domain and type can be retrieved by the *find()* method if the manager offers this method:

```php
$item = $manager->find( $code );
$item = $manager->find( $code, ['text'], $domain, $type );
```

The first call will return the item for the given code, provided the code alone is unique. This works for categories, coupon codes, customers, customer groups, locale sites, products, stocks and suppliers. If the code isn't unique enough, you will need to supply domain and type as well. Domain items that can be fetched this way are attributes and services and all kind of type items.

The second argument for retrieving the associated items, too, is the same as described for [getting an item](#get-item).

## Search items

Several items can be retrieved at once via the `search()` method. It enables you to specify criteria to exactly get the items you need. To create a required criteria object, use the `filter()` method:

```php
$filter = $manager->filter();
$filter = $manager->filter( true );
```

This method will add default criteria (e.g. the status of entries must be "1") to the new object if *true* is passed as argument. For details about filtering have a look at the article about [search filters](search-filter.md).

This filter object must then be passed to the `search()` method as first parameter:

```php
$total = 0;
$items = $manager->search( $filter );
$items = $manager->search( $filter, ['text'] );
$items = $manager->search( $filter, ['attribute' => ['variant']] );
$items = $manager->search( $filter, [], $total );
```

The second argument lists the names of the associated domains whose items should be fetched, too. You can either get all referenced items of the given domain or limit the items by the list type(s) of the reference. This works the same as [getting an item](#get-item).

The last argument is a value/result parameter which will contain the total number of items matching the search criteria. By default, only the first 100 items are returned.

## Iterate items

Since 2022.10, some managers (e.g. index and product managers) are implementing the `iterator()` and `iterate()` methods which should be used if you need to fetch all records subsequently:

```php
$manager = \Aimeos\MShop::create( $this->context(), 'product' );
$iterator = $manager->iterator( $manager->filter() );

while( $items = $manager->iterate( $iterator, ['text'], 100 ) ) {
    // process items
}
```

First, you have to create an iterator object from the filter. The filter can contain all conditions and sorting possibilities also available when using `search()`. Pass this iterator to the `iterate()` method to retrieve all items subsequently. The second paramter contains the names of the associated domains whose items should be fetched, too. The third parameter is the maximum number of items which should be returned at once. Only the first parameter of `iterate()` is required, the other ones are optional.

## Delete items

The last action in the life cycle of an item is to delete it from the storage if it's not needed anymore. Managers offer the method `delete()` to remove entries:

```php
$manager->delete( $id );
$manager->delete( $ids );
$manager->delete( $item );
$manager->delete( $items );
```

The method `delete()` can remove a single entry or multiple entries by ID as well as a single item or multiple items at once, which is preferable to reduce the number of executed statements.

# Manage related items

## Referenced items

For domains which have a list table, you can reference items from other domains and retrieve them together with the item when using `get()`, `find()` or `search()`.

Referencing foreign items is available for these domains:

* attribute
* catalog
* customer
* media
* price
* product
* service
* supplier
* text

The managers of those domains implement a `createListItem()` method which creates a new list item:

```php
$listitem = $manager->createListItem();
```

Then you can set the required ID of the foreign domain in order to add the list item to the domain item:

```php
$item = $manager->create();
$item->addListItem( 'attribute', $listitem->setRefId( '123' ) );
$item->addListItem( 'attribute', $listitem->setRefId( '123' ), $refItem );
```

The first argument must be the name of the referenced domain ("attribute" in this case). The second call to `addListItem()` contains the referenced item as third argument (`$refitem`) which is then added to the list item and will be saved automatically when calling `save()` of the manager.

There are more properties of the list item you can set using:

setType()
: Type of the list item (default: "default") in case you need to distinguish between references to the same foreign domain. For example, selection products reference article products, but can also reference suggested products (type: "suggestion") or products bought together (type: "bought-together")

setConfig()
: Arbitrary list of key/value pairs you can use to store additonal information

setDateStart()
: Start date when the list item should be used in the frontend. Can be used to limit referenced items to a certain time frame

setDateEnd()
: End date till when the list item should be used in the frontend. Can be used to limit referenced items to a certain time frame

setStatus()
: Enables (value: 1) or disables (value: 0) the list item (default: 1)

To retrieve the list items you can use:

```php
$listitems = $item->getListItems();
$listitems = $item->getListItems( 'attribute' );
$listitems = $item->getListItems( 'attribute', 'default' );
$listitems = $item->getListItems( 'attribute', 'default', 'color' );
$listitems = $item->getListItems( 'attribute', 'default', 'color', false );
```

The first line will return all list items regardless of which domains they reference, while the second one only returns the list items for the given domain. The third example additionally limits the list items by their types, and the fourth example only returns attributes of type "color". The last line will return all items, even if they shouldn't be shown in the frontend.

Arguments one to three can be a string like in the given examples above, *null* for any value, or an array of values.

To return a list item for a specific domain, type and ID, you should call:

```php
$listitem = $item->getListItem( 'attribute', 'color', '123' );
$listitem = $item->getListItem( 'attribute', 'color', '123', false );
```

For items returned by `get()`, `find()` or `search()` with a list of domains to fetch as second parameter, you can also retrieve the referenced items directly:

```php
$refitems = $item->getRefItems();
$refitems = $item->getRefItems( 'attribute' );
$refitems = $item->getRefItems( 'attribute', 'color' );
$refitems = $item->getRefItems( 'attribute', 'color', 'default' );
$refitems = $item->getRefItems( 'attribute', 'color', 'default', false );
```

The arguments are the same as for `getListItems()`, only the list type and type of the referenced item is reversed and the method returns the referenced items instead of the list items (attributes in this example). The first three arguments can be *null* or of type string or array like for `getListItems()`.

Finally, it's also possible to remove list references again using:

```php
$item->deleteListItem( 'attribute', $listitem );
$item->deleteListItem( 'attribute', $listitem, $refitem );
```

This removes the given list items. The second line will delete the referenced item, too. You can also delete several list items at once, provided their "domain" is set:

```php
$item->deleteListItems( $listitems );
$item->deleteListItems( $listitems, true );
```

The first line removes the given list items while the second one also removes the referenced items.

!!! warning
    Removing the referenced items, too, is useful for domains whose items are associated to once only (e.g. texts, prices) but should not be done for e.g. "attribute".

## Properties

Properties are key/language/value pairs which you can use to store arbitrary data. The following data domains support properties:

* attribute
* customer
* media
* price
* product

The managers of those domains implement a `createPropertyItem()` method, which creates a new property item:

```php
$propitem = $manager->createPropertyItem();
```

Once created you can set the type, language (optional) and value:

```php
$propItem->setType( 'erp-id' )->setValue( 'ABCD-1234' );

// or example with language ID:
$propItem->setType( 'title' )
    ->setLanguageId( 'en' )
    ->setValue( 'My product' );
```

Add or set the property item to the domain item:

```php
$item = $manager->create();
$item->addPropertyItem( $propitem );
$item->setPropertyItems( [$propitem] );
```

The second line will add the property item without overwriting the existing propery items. The third line will remove all existing property items before adding the new list of items.

To retrieve property items, you can use:

```php
$propitems = $item->getPropertyItems();
$propitems = $item->getPropertyItems( '<type>' );
$propitems = $item->getPropertyItems( null, false );
```

The first line will return all property items of the domain item while the second line will only return the property items of the type passed as first argument. The third line will return all property items, even if they should not be shown in the frontend. The list of property items returned is a [Map object](https://github.com/aimeos/map).

It's also possible to return the property values without the items using:

```php
$values = $item->getProperties( '<type>' );
```

The content of `$values` is also a [Map object](https://github.com/aimeos/map).

You can also remove one or more property items from the domain item again:

```php
$item->deletePropertyItem( $propitem );
$item->deletePropertyItems( [$propitem] );
```

To clear all property items, simple pass an empty array ([]) to `setPropertyItems()`.

## Attribute vs. properties

The difference between attributes and properties is rather easy:

* Attributes can be shared between products and build facets for filtering
* Properties are not shared and are only available for one product

Examples:

* "size" is an attribute because the attribute values are used by all clothing products
* "isbn" is a property because it's only relevant for one book

There might be gray areas where it's not so clear if you should use attributes or properties. In this case prefer properties over attributes, if you don't need it to build facets, for performance reasons.

Attributes are referenced in the *mshop_product_list* table, and so are media, texts, prices, etc. If you have millions of entries in the lists table an only thousands in the mshop_product_property table, then your performance might be lower than in could be due to MySQL selecting sometimes the wrong index.
