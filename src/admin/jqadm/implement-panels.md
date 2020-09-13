You can implement a new panel for managing additional data of a new data domain you've created or for a foreign table editors should be able to administrate. In the first case, you need to [create the manager and item](../../infrastructure/managing-items.md) first. To manage a foreign table, you can also use the raw database connection from the [Aimeos context](../../infrastructure/context.md) if you want.

# Factory class

First you need to create a `Factory.php` class in the `./admin/jqadm/src/Admin/JQAdm/Mypanel/` directory. It's reponsible for instantiating the panel class, allows replacing your class by configuration and add configured decorators to the instantiated object.

Use this example factory and replace `Mypanel` and `mypanel` by the name of your panel. The first character of the name in the namespace and classname part must be upper case, all other occurences must be in lower case.

```php
namespace Aimeos\Admin\JQAdm\Mypanel;

class Factory
    extends \Aimeos\Admin\JQAdm\Common\Factory\Base
    implements \Aimeos\Admin\JQAdm\Common\Factory\Iface
{
    public static function create( \Aimeos\MShop\Context\Item\Iface $context, string $name = null ) : \Aimeos\Admin\JQAdm\Iface
    {
        if( $name === null ) {
            $name = $context->getConfig()->get( 'admin/jqadm/mypanel/name', 'Standard' );
        }

        $iface = '\\Aimeos\\Admin\\JQAdm\\Iface';
        $classname = '\\Aimeos\\Admin\\JQAdm\\Mypanel\\' . $name;

        if( ctype_alnum( $name ) === false ) {
            throw new \Aimeos\Admin\JQAdm\Exception( sprintf( 'Invalid characters in class name "%1$s"', $classname ) );
        }

        $client = self::createAdmin( $context, $classname, $iface );

        return self::addClientDecorators( $context, $client, 'mypanel' );
    }
}
```

# Class structure

The panel class will do the real work. Create a `Standard.php` class in the `./admin/jqadm/src/Admin/JQAdm/Mypanel/` directory like this skeleton class. Also, replace `Mypanel` and `mypanel` by the name of your panel like in the factory class.

```php
namespace Aimeos\Admin\JQAdm\Mypanel;

sprintf( 'mypanel' ); // for translation

class Standard
    extends \Aimeos\Admin\JQAdm\Common\Admin\Factory\Base
    implements \Aimeos\Admin\JQAdm\Common\Admin\Factory\Iface
{
    public function copy() : ?string
    {
        return parent::copy();
    }

    public function create() : ?string
    {
        return parent::create();
    }

    public function delete() : ?string
    {
        return parent::delete();
    }

    public function export() : ?string
    {
        return parent::export();
    }

    public function get() : ?string
    {
        return parent::get();
    }

    public function save() : ?string
    {
        return parent::save();
    }

    public function search() : ?string
    {
        return parent::search();
    }

    public function getSubClient( string $type, string $name = null ) : \Aimeos\Admin\JQAdm\Iface
    {
        return $this->createSubClient( 'mypanel/' . $type, $name );
    }

    protected function getSubClientNames() : array
    {
        return $this->getContext()->getConfig()->get( 'admin/jqadm/mypanel/standard/subparts', [] );
    }
}
```

All methods beside the last two are optional and default implementations exist in the base class, so you only have to implement the methods you really need. The `getSubClient()` and `getSubClientNames()` will care about creating the configured subparts, so your component can be extended dynamically.

# Parameters and files

When the class is instantiated, a view object containing the passed GET and POST parameters as well as the uploaded files is added to the object. It should also be used to render the template after more data has been assigned to the view. You can access the view and the parameters using:

```php
$view = $this->getView();
$param = $view->param(); // all parameters
$array = $view->param( 'item', [] ); // all item[...] parameters sent or empty array
$value = $view->param( 'item/mydomain.status', 1 ); // single value for item[mydomain.status]
```

To get the uploaded files use:

```php
$view = $this->getView();
$files = (array) $view->request()->getUploadedFiles();
```

The file objects implement the [PSR-7](https://www.php-fig.org/psr/psr-7/#16-uploaded-files) `\Psr\Http\Message\UploadedFileInterface` which is much simpler to handle correctly than using `$_FILES` directly. The most important methods of the objects are:

```php
if( $file->getError() !== UPLOAD_ERR_NO_FILE
    && $file->getError() === UPLOAD_ERR_OK
) {
    $file->moveTo( '/path/to/new/filename' );
    $stream = $file->getStream();
    $content = (string) $stream; // don't do that for large files
}
```

You can use the Aimeos file system manager to store uploaded files regardless if it's on a local disc or in the cloud:

```php
$fs = $this->getContext()->fs( 'fs-import' );
$fs->writes( '/path/to/file', $file->getStream()->detach() );
```

# Class methods

## copy()

When the editor wants to copy an item, the ID of the item will be available as parameter. Instead of storing a copy of the item instantly, the `copy()` method should load the item data included all related data displayed in the panel.

If you pass the data to the template, the view will render the form for the detail view of the panel including the data. Thus, the editor can modify the data and store them when clicking on the "Save" button.

```php
public function copy() : ?string
{
    $view = $this->getView();

    try
    {
        $manager = \Aimeos\MShop::create( $this->getContext(), 'mydomain' );
        $view->item = $manager->get( $this->require( 'id' ), ['text', /* ... */] );

        $data = $view->item->toArray( true );
        $data['mydomain.siteid'] = $this->getContext()->locale()->getSiteId();
        $data['mydomain.code'] = $data['mydomain.code'] . '_copy';
        $data['mydomain.id'] = '';

        $view->itemData = $data;
        $view->itemBody = parent::copy();
    }
    catch( \Exception $e )
    {
        $this->report( $e, 'copy' );
    }

    $tplconf = 'admin/jqadm/mypanel/template-item';
    $default = 'mypanel/item-standard';

    return $view->render( $view->config( $tplconf, $default ) );
}
```

Retrieve the required ID, then fetch the item from the storage and use `toArray(true)` to retrieve a simple array of key/value pairs. There are three things to keep in mind when an item should be copied in Aimeos:

* The `....siteid` value must be set to the ID of the current site
* If the item must contain an unique value, add `_copy` to the existing one
* Reset the ID to an empty string to create a new record in the storage

Besides the modified record data, you should also call `parent::copy()` and assign the return value to the view. This will contain the forms of the subparts if there are any (in the future).

If an exception occurs, use `$this->report($e, 'copy')` to log the exception and show an appropriate error message in the backend. Do not render the view inside the try/catch block because the editor won't get any output in that case.

At the end, render the view with `$view->render()` to create the HTML output for the detail view. Use `$view->config()` to make the used template configurable. The first parameter is the configuration key, the second parameter is the default value if no alternative template path is configured.

## create()

Creating an item doesn't add a new record in the storage immediately. Instead, the `create()` method must instantiate a new item and pass the output of `toArray()` to the template. This will render the form in the detail view of your panel including the default values from the item.

When the editor has filled in the required data into the input fields and click on the "Save" button, the new data will be saved to the storage.

```php
public function create() : ?string
{
    $view = $this->getView();

    try
    {
        if( !isset( $view->item ) ) {
            $view->item = \Aimeos\MShop::create( $this->getContext(), 'mydomain' )->create();
        }

        $data = $view->param( 'item', [] );
        $data['mydomain.siteid'] = $view->item->getSiteId();

        $view->itemData = array_replace_recursive( $this->toArray( $view->item, true ), $data );
        $view->itemBody = parent::create();
    }
    catch( \Exception $e )
    {
        $this->report( $e, 'create' );
    }

    $tplconf = 'admin/jqadm/mypanel/template-item';
    $default = 'mypanel/item-standard';

    return $view->render( $view->config( $tplconf, $default ) );
}
```

Check if there's an existing item assigned to the view first because if an error occurs in `save()` the `create()` method will be called afterwards. If it doesn't exist, create one with the appropriate manager.

Retrieve the parameters from the browser and reset the `....siteid` value which the ID from the item. Then, call `toArray(true)` to get a simple array of key/value pairs that you can merge recursively with the data from the browser.

Besides the data, you should also call `parent::create()` and assign the return value to the view. This will contain the forms of the subparts if there are any (in the future).

If an exception occurs, use `$this->report($e, 'create')` to log the exception and show an appropriate error message in the backend. Do not render the view inside the try/catch block!

At the end, render the view with `$view->render()` to create the HTML output for the detail view. Use `$view->config()` to make the used template configurable. The first parameter is the configuration key, the second parameter is the default value if no alternative template path is configured.

## delete()

To delete one or more items, their IDs must be passed by the HTML template. The required code is a bit more than expected to enable subparts to delete related items too:

```php
public function delete() : ?string
{
    $view = $this->getView();

    $manager = \Aimeos\MShop::create( $this->getContext(), 'mydomain' );
    $manager->begin();

    try
    {
        $ids = (array) $this->require( 'id' );
        $search = $manager->filter()->add( 'mydomain.id', '==', $ids );
        $items = $manager->search( $search->slice( 0, count( $ids ) ) );

        foreach( $items as $item )
        {
            $view->item = $item;
            parent::delete();
        }

        $manager->delete( $items->toArray() );
        $manager->commit();

        return $this->redirect( 'mypanel', 'search', null, 'delete' );
    }
    catch( \Exception $e )
    {
        $manager->rollback();
        $this->report( $e, 'delete' );
    }

    return $this->search();
}
```

When deleting items, you should always wrap the operations into a transaction. This avoids deleting records partially and improves performance because the data is only synced once to the storage.

Retrieve the required ID or IDs, then fetch the item or items from the storage. You need to assign the items one by one to the view and call `parent::delete()` so the subparts have access to the item and delete related data too.

Now delete the fetched items and commit your transaction if everything is fine. Send a redirect to the browser to the list view using `$this->redirect()`. It's parameters are:

* Resource to redirect too (usually the same as the deleted one)
* Action to perform (usually *search* to render the list view)
* ID of the item (none in this case)
* Current action (here: *delete*)

If something fails, roll back the transaction and use `$this->report($e, 'delete')` to log and show an appropriate error message. At the end, call `$this->search()` to return the list view that will be shown to the editor afterwards.

## export()

For exporting files, you have to implement the `export() method. This method shouldn't create the file directly and return it to the browser immediately because creating the file can be a resource intensive task.

Instead, you should send the request for exporting the data to a message queue and implement a [job controller](../../cronjobs/create-job-controller.md) that does the actual work. There's a widget in the dashboard that will show the exported file afterwards.

```php
public function export() : ?string
{
    $view = $this->getView();
    $context = $this->getContext();

    try
    {
        $msg = ['sitecode' => $context->getLocale()->getSiteItem()->getCode()];

        if( $filter = $view->param( 'filter' ) ) {
            $msg['filter'] = $this->getCriteriaConditions( (array) $filter );
        }

        if( $sort = $view->param( 'sort' ) ) {
            $msg['sort'] = $this->getCriteriaSortations( (array) $sort );
        }

        $queue = $view->param( 'queue', 'myexportqueue' );
        $mq = $context->queue( 'mq-admin', $queue );
        $mq->add( json_encode( $msg ) );

        $msg = $context->i18n()->dt( 'admin', 'Your export will be available in a few minutes for download' );
        $view->info = $view->get( 'info', [] ) + ['mypanel-item' => $msg];
    }
    catch( \Exception $e )
    {
        $this->report( $e, 'export' );
    }

    return $this->search();
}
```

Usually, you want to limit the exported data to the current filters and use the sort order selected in the list view. Therefore, you should retrieve the *filter* and *sort* parameters and push them together with the site code to the message queue.

The format of the message must be structured depending on what your job controller expects. It must be serialized because only strings can be passed to message queues and the JSON output generated by `json_ecode()` is a portable format.

You can retrieve the message queue for adding the message by using `$context->queue( 'mq-admin', $queue )`. The first parameter should be always *'mq-admin'* because this is the message resource configured for the admin backend. The queue name can be an arbitrary string, that must be different for each panel and type of export you want to create and must match the name that the job controller expects.

If editors should be able to create two or more export types, you have to use the queue name passed from the list view of the panel. After adding the message to the queue, you must give the editor a hint that the export will be available later in the dashboard.

If an exception occurs, use `$this->report($e, 'export')` to log the exception and show an appropriate error message in the backend.At the end, call `$this->search()` to return the list view that will be shown to the editor afterwards.

## get()

This method is used to retrive the data for the detail view of the panel. It's pretty straight forward to implement:

```php
public function get() : ?string
{
    $view = $this->getView();

    try
    {
        $manager = \Aimeos\MShop::create( $this->getContext(), 'mydomain' );

        $view->item = $manager->get( $this->require( 'id' ), ['text', /* ... */] );
        $view->itemData = $this->toArray( $view->item );
        $view->itemBody = parent::get();
    }
    catch( \Exception $e )
    {
        $this->report( $e, 'get' );
    }

    $tplconf = 'admin/jqadm/mypanel/template-item';
    $default = 'mypanel/item-standard';

    return $view->render( $view->config( $tplconf, $default ) );
}
```

Retrieve the required ID, then fetch the item from the storage and use `toArray(true)` to retrieve a simple array of key/value pairs. Call `parent::get()` and assign the return value to the view. This will contain the forms of the subparts if there are any (in the future).

If an exception occurs, use `$this->report($e, 'get')` to log the exception and show an appropriate error message in the backend.

At the end, render the view with `$view->render()` to create the HTML output for the detail view. Use `$view->config()` to make the used template configurable. The first parameter is the configuration key, the second parameter is the default value if no alternative template path is configured.

## save()

This method actually adds or updates the item in the storage using the data passed from the form in the detail view.

```php
public function save() : ?string
{
    $view = $this->getView();
    $context = $this->getContext();

    $manager = \Aimeos\MShop::create( $context, 'mydomain' );
    $manager->begin();

    try
    {
        if( $id = $data['mydomain.id'] ?? null ) {
            $item = $manager->get( $id, ['text', /* ... */] );
        } else {
            $item = $manager->create();
        }

        $item = $item->fromArray( $view->param( 'item', [] ), true );
        $view->item = $item->getId() ? $item : $manager->save( $item );
        $view->itemBody = parent::save();

        $item = $manager->save( clone $view->item );
        $manager->commit();

        return $this->redirect( 'mypanel', $view->param( 'next' ), $view->item->getId(), 'save' );
    }
    catch( \Exception $e )
    {
        $manager->rollback();
        $this->report( $e, 'save' );
    }

    return $this->create();
}
```

You should always wrap the operations into a transaction. This avoids saving records partially and improves performance because the data is only synced once to the storage.

If the ID of the item is passed, you have to fetch the item and otherwise, create an empty item. Then, you can merge the data with the existing item values and save the item if it doesn't have an ID yet. This is important because the subparts which have access to `$view->item` when calling `parent::save()` will need the ID of the item to perform their own tasks.

After the subparts added their own content to the item, save a copy of it again. Using a copy is important if something goes wrong and the related items are only partially saved, but they already contain IDs. This would lead to problems if the editor clicks on save in the detail view again because those items wouldn't be saved at all!

!!! tip
    Here's also a good place to store uploaded files for importing them. Use `$view->request()->getUploadedFiles()` and the methods described in the [parameters and files](#parameters-and-files) section.

When everything is fine, commit the transaction and redirect the browser to the next page. The redirect depends on the *next* parameter sent by the "Save", "Save & close" or "Save & copy" button. The parameters for `$this->redirect()` are:

* Resource to redirect too (usually the same as the saved one)
* Action to perform (depends on the *next* parameter)
* ID of the saved item
* Current action (here: *save*)

In case of an error, roll back the transaction and use `$this->report($e, 'save')` to log and show an appropriate error message. At the end, call `$this->create()` to show the detail view including the data entered by the editor again.

## search()

The `search()` method creates the list view and is also used for every default view even if it's not showing a list of items. For example, the HTML for the graph container in the dashboard is also generated this method.

```php
public function search() : ?string
{
    $view = $this->getView();

    try
    {
        $total = 0;
        $params = $this->storeFilter( $view->param(), 'mydomain' );
        $manager = \Aimeos\MShop::create( $this->getContext(), 'mydomain' );

        $filter = $manager->filter()->sort( 'mydomain.id' );
        $filter = $this->initCriteria( $filter, $params );

        $view->items = $manager->search( $filter, ['text', /* ... */], $total );
        $view->filterAttributes = $manager->getSearchAttributes( true );
        $view->filterOperators = $filter->getOperators();
        $view->itemBody = parent::search();
        $view->total = $total;
    }
    catch( \Exception $e )
    {
        $this->report( $e, 'search' );
    }

    $tplconf = 'admin/jqadm/mypanel/template-list';
    $default = 'mypanel/list-standard';

    return $view->render( $view->config( $tplconf, $default ) );
}
```

To display the used filter settings after rendering the list view, you should store them in the session using `$this->storeFilter()`. You can then retrieve them in the template using `$this->session('aimeos/admin/jqadm/mypanel/fields')` again.

Then, create a filter object and set the default sorting before passing the object to `$this->initCriteria()` which updates the filter according to the passed parameters. Hand over the filter to the `search()` method of the manager and don't forget the third argument, which will contain the total number of found items and which should be assigned to the view too.

The search filter attributes and operators returned by the manager should be passed to the view too if applicable. They are necessary to offer the global filter in the upper right corner of the list view.

If an exception occurs, use `$this->report($e, 'create')` to log the exception and show an appropriate error message in the backend. Do not render the view inside the try/catch block!

At the end, render the view with `$view->render()` to create the HTML output for the list view. Use `$view->config()` to make the used template configurable. The first parameter is the configuration key, the second parameter is the default value if no alternative template path is configured.

# Configuration

## Navigation

To add your panel to the left navigation bar, you have to overwrite the `admin/jqadm/navbar` configuration setting and add your panel name at the appropriate position:

```php
return [
    'dashboard',
    'order',
    'customer',
    'product',
    'catalog',
    'attribute',
    'mypanel',
    'coupon',
    'subscription',
    'supplier',
    'service',
    'plugin',
    'group',
    'locale' => [
        'locale',
        'locale/site',
        'locale/language',
        'locale/currency',
    ],
    'type' => [
        'type/attribute',
        'type/attribute/lists',
        'type/attribute/property',
        'type/catalog/lists',
        'type/customer/lists',
        'type/customer/property',
        'type/media',
        'type/media/lists',
        'type/media/property',
        'type/plugin',
        'type/price',
        'type/price/lists',
        'type/price/property',
        'type/product',
        'type/product/lists',
        'type/product/property',
        'type/service',
        'type/service/lists',
        'type/stock',
        'type/tag',
        'type/text',
        'type/text/lists',
    ],
    'log',
];
```

Please have a look at the articles about how to overwrite the configuration in [Laravel](../../laravel/customize.md#change-configuration),  [Symfony](../../symfony/customize.md#change-configuration) and [TYPO3](../../typo3/customize.md#change-configuration).

## Permissions

You also need to configure who is allowed to access your panel. Therefore, add this to your `admin/jqadm/resource` configuration:

```
'mypanel' => [
    'groups' => ['editor', 'admin', 'super'],
],
```

Available groups are:

editor
: Editor with limited access who can only manage content but isn't allowed to change any shop configuration

admin
: Site admins who can manage all settings and content for their own site

super
: Super user who can see and manage all settings and content from all sites

You need to add at least the *super* group for your panel and you should either use `['editor', 'admin', 'super']`, `['admin', 'super']` or `['super']` for the *group* configuration.

Please have a look at the articles about how to overwrite the configuration in [Laravel](../../laravel/customize.md#change-configuration),  [Symfony](../../symfony/customize.md#change-configuration) and [TYPO3](../../typo3/customize.md#change-configuration).

# Templates

For the required list and detail view templates, please have a look at the [JQAdm template](panel-templates.md) article.
