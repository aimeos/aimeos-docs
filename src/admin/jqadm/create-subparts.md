Implementing subparts is a great way to allow editors to manage additional data related to the main panel. You can fetch data from other sources to make it editable together with the item data and save both after the editor clicked on "Save". The subparts get their own tab in the panel so editors are not confused even if a lot of data can be edited like in the product panel.

# Class structure

The sub-panel class structure is the same as for the panel itself. Create a `Standard.php` class in the `./admin/jqadm/src/Admin/JQAdm/Mypanel/Mysubpanel` directory like this skeleton class. Also, replace `Mysubpanel` and `mysubpanel` by the name of your panel.

```php
namespace Aimeos\Admin\JQAdm\Mypanel\Mysubpanel;

sprintf( 'mysubpanel' ); // for translation

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
        return $this->createSubClient( 'mypanel/mysubpanel/' . $type, $name );
    }

    protected function getSubClientNames() : array
    {
        return $this->context()->getConfig()->get( 'admin/jqadm/mypanel/mysubpanel/subparts', [] );
    }
}
```

All methods beside the last two are optional and default implementations exist in the base class, so you only have to implement the methods you really need. The `getSubClient()` and `getSubClientNames()` will care about creating the configured subparts, so your subpart can be extended dynamically.


# Class methods

## copy()

When the items managed in the subpart should be copied too, you only need to retrieve them in the `copy()` method and don't add the ID of those items in the template.

If you pass the data to the template, the view will render the form fields for the subpart in the detail view of the panel including the data. Thus, the editor can modify the data and store them when clicking on the "Save" button.

```php
public function copy() : ?string
{
    $data = [];
    $view = $this->view();
    $siteid = $this->context()->getLocale()->getSiteId();
    $manager = \Aimeos\MShop::create( $this->context(), 'somedomain' );

    foreach( $manager->search( $manager->filter() ) as $item )
    {
        $entry = $item->toArray( true );
        $entry['somedomain.siteid'] = $siteId;
        $entry['somedomain.id'] = '';
        $data[] = $entry;
    }

    $view->mysubpanelData = $data;
    $view->mysubpanelBody = parent::copy();

    $tplconf = 'admin/jqadm/mypanel/mysubpanel/template-item';
    $default = 'mypanel/item-mysubpanel-standard';

    return $view->render( $view->config( $tplconf, $default ) );
}
```

Fetch the data you need from the storage and reset the *siteid* and *id* values, so they are stored again using the current site ID and a new ID. You should also call `parent::copy()` and assign the return value to the view. This will contain the forms of further subparts if there are any (in the future).

At the end, render the view with `$view->render()` to create the HTML output for the detail view. Use `$view->config()` to make the used template configurable. The first parameter is the configuration key, the second parameter is the default value if no alternative template path is configured.

## create()

The `create()` method must not add a new record in the storage. Instead, it's template will render empty input fields or populate them the data from the request in case of an error. After the editor has filled in the required data and click on the "Save" button, the new data will be stored in the `save()` method.

```php
public function create() : ?string
{
    $view = $this->view();
    $data = $view->param( 'mysubpanel', [] );
    $siteid = $this->context()->getLocale()->getSiteId();

    foreach( $view->value( $data, 'somedomain.id', [] ) as $idx => $value ) {
        $data[$idx]['mysubpanel.siteid'] = $siteid;
    }

    $view->mysubpanelData = $data;
    $view->mysubpanelBody = parent::copy();

    $tplconf = 'admin/jqadm/mypanel/mysubpanel/template-item';
    $default = 'mypanel/item-mysubpanel-standard';

    return $view->render( $view->config( $tplconf, $default ) );
}
```

Retrieve the parameters from the browser and reset the `....siteid` value which the ID from the locale item. You should also call `parent::create()` and assign the return value to the view. This will contain the forms of the subparts if there are any (in the future).

At the end, render the view with `$view->render()` to create the HTML output for the detail view. Use `$view->config()` to make the used template configurable. The first parameter is the configuration key, the second parameter is the default value if no alternative template path is configured.

## delete()

To remove the items managed by the subpart, you can delete their items based on the data of the passed item.

```php
public function delete() : ?string
{
    parent::delete();

    $itemId = $this->view()->item->getId();

    $manager = \Aimeos\MShop::create( $this->context(), 'somedomain' );
    $filter = $manager->filter()->add( ['somedomain.foreignid' => $itemId] );
    $manager->delete( $manager->search( $filter ) );

    return null;
}
```

First, call `parent::delete()` so the subparts have access to the item and can delete related data too.

The view contains a property `item` which contains the full item from the main panel that should be deleted. You can use it to find and delete the records managed by your subpart.

You don't need to return a template because it wouldn't be used, so return *null*. The browser gets redirected to the list page by the main panel.

## export()

Usually, passing the filter parameters to the job controller via the message queue is only done by the main panel. Thus, you don't have to implement anything in the subpart. Nevertheless, the `export()` method of the subpart will be called if an export is requested if you have special needs and the same parameters are available as in the [export() method of the main panel](implement-panels.md#export).

## get()

This method is used to retrive the data shown in the subpart of the detail view for the panel:

```php
public function get() : ?string
{
    $data = [];
    $view = $this->view();
    $context = $this->context();
    $siteId = $context->getLocale()->getSiteId();

    $manager = \Aimeos\MShop::create( $context, 'somedomain' );
    $filter = $manager->filter()->add( ['somedomain.foreinid' => $view->item->getId()] );

    foreach( $manager->search( $filter ) as $item ) {
        $data[] = $item->toArray( true );
    }

    $view->mysubpanelData = $data;
    $view->mysubpanelBody = parent::get();

    $tplconf = 'admin/jqadm/mypanel/mysubpanel/template-item';
    $default = 'mypanel/item-mysubpanel-standard';

    return $view->render( $view->config( $tplconf, $default ) );
}
```

You have access to the item from the main panel and can use its properties to fetch the related items from the storage. Use `toArray(true)` to get a simple array of key/value pairs you assign to the view. Call `parent::get()` and assign the return value too. This will contain the forms of the subparts if there are any (in the future).

At the end, render the view with `$view->render()` to create the HTML output for the detail view. Use `$view->config()` to make the used template configurable. The first parameter is the configuration key, the second parameter is the default value if no alternative template path is configured.

## save()

Here, the newly entered or updated data from the form in the detail view is actually saved to the storage. If the entries already contain an ID, update them, create new records otherwise.

```php
public function save() : ?string
{
        $view = $this->view();

        $manager = \Aimeos\MShop::create( $this->context(), 'somedomain' );
        $manager->begin();

        try
        {
            $filter = $manager->filter()->add( ['somedomain.foreinid' => $view->item->getId()] );
            $items = $manager->search( $filter );
            $list = [];

            foreach( $view->param( 'mysubpanel', [] ) as $entry )
            {
                $id = $this->val( $entry, 'somedomain.id' );

                $list[] = $items->get( $id, $manager->create() )
                    ->fromArray( $entry )
                    ->setParentId( $view->item->getId() );

                $items->remove( $id );
            }

            $manager->delete( $items );
            $manager->save( $list, false );
            $manager->commit();

            parent::save();
        }
        catch( \Exception $e )
        {
            $manager->rollback();
            throw $e;
        }

        return null;
}
```

You should always wrap the operations into a transaction. This avoids saving records partially and improves performance because the data is only synced once to the storage.

Fetch the related items first so you know which records are currently associated to the item. Then, loop over the data sent by the browser and retrieve the ID if there's any, so we know we have to update or create the item. Now, you can use `get()` to return the item if there's already one in `$items` or create a new one if not. Use `fromArray()` to populate the item with the new data and set the property by which you know the record belongs to the item from the main panel (here: `setParentId()`).

Store the updated item in a separate list because now you remove the item from the original `$items` map. Thus, you can then delete all left over items because they have been removed by the editor and are not part of the data sent by the browser any more. Save the updated/created items and commit the transation.

When everything is fine, commit the transation and call `parent::save()` to execute the `save()` methods of subparts to this one too. You don't have to return anything besides *null* because the main panel already cares about that.

## search()

Usually, Implementing the `search()` method isn't necessary because subparts don't add data to the list view.

# Template

A subpart template is almost the same as the [panel item template](panel-templates.md#basic-tab). The structure is exactly the same and you can use the same code for adding input/select fields. Just replace and "mysubpanel" with your subpart name (case sensitiv):

```php
<?php
    $enc = $this->encoder();
?>
<div id="mysubpanel" class="item-mysubpanel tab-pane fade" role="tabpanel" aria-labelledby="mysubpanel">

    <div class="box">
        <div class="row">
            <div class="col-xl-6 vue <?= $this->site()->readonly( $this->get( 'mysubpanelData/mysubpanel.siteid' ) ); ?>"
                data-data="<?= $enc->attr( $this->get( 'mysubpanelData', new stdClass() ) ) ?>">

                <!-- input/select fields -->
            <div>
        <div>
    <div>

    <?= $this->get( 'mysubpanelBody' ); ?>
</div>
```

Notes on subpart templates:

tab pane
: The first `<div>` is for the Boostrap tab and must not be the root of the Vue.js application

vue
: In the second `<div>`, the Vue applcation is initialized because it contains the `vue` class. The Aimeos JS creates a Vue instance for each HTML node that contains the class. You can add arbitrary data to the Vue instance in the `data-data="..."` attribute, which must contain a valid Javascript object (`{}`). Remove the `vue` CSS class if you don't use Vue.js components in your subpart

further subparts
: Include the `<?= $this->get( 'mysubpanelBody' ); ?>` to allow other extensions to add more subparts to yours

# Configuration

To show your new subpart in the panel, you have to add the subpart name to the subparts configuration for that panel in the `./config/admin.php` file of your extension:

```php
return [
    'jqadm' => [
        'mypanel' => [
            'subparts' => [
                'mysubpanel' => 'mysubpanel'
            ]
        ]
    ]
];
```

!!! note
    Merge the configuration above with the existing configuration in that file if there is any!

For existing panels like the product detail panel, only change the panel name:

```php
return [
    'jqadm' => [
        'product' => [
            'subparts' => [
                'mysubpanel' => 'mysubpanel'
            ]
        ]
    ]
];
```

!!! warn
    You can only configure the subpanel for the main panel it's written for according to its namespace! Configuring your subpart for a foreign panel doesn't work and will result in an error that the subpart isn't found.
