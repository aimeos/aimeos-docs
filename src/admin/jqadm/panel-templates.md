# List template

The list template for a panel must be stored in your own Aimeos extension in `./templates/admin/jqadm/<panel name>/list.php` and consists of the

* navigation bar including the global search
* top and bottom pagination
* form with content table

You can use this base template for your own one but you must replace "Mypanel" and "mypanel" with your panel name (case sensitiv):

```php
<?php
    $enc = $this->encoder();

    $target = $this->config( 'admin/jqadm/url/search/target' );
    $controller = $this->config( 'admin/jqadm/url/search/controller', 'Jqadm' );
    $action = $this->config( 'admin/jqadm/url/search/action', 'search' );
    $config = $this->config( 'admin/jqadm/url/search/config', [] );

    $searchParams = $params = $this->get( 'pageParams', [] );
    $searchParams['page']['start'] = 0;
?>
<?php $this->block()->start( 'jqadm_content' ); ?>
<div class="vue-block">
    <nav class="main-navbar">
        <span class="navbar-brand">
            <?= $enc->html( $this->translate( 'admin', 'Mypanel' ) ); ?>
            <span class="navbar-secondary">(<?= $enc->html( $this->site()->label() ); ?>)</span>
        </span>

        <?= $this->partial(
            $this->config( 'admin/jqadm/partial/navsearch', 'common/partials/navsearch' ), [
                'filter' => $this->session( 'aimeos/admin/jqadm/mypanel/filter', [] ),
                'filterAttributes' => $this->get( 'filterAttributes', [] ),
                'filterOperators' => $this->get( 'filterOperators', [] ),
                'params' => $params,
            ]
        ); ?>
    </nav>

    <?= $this->partial(
            $this->config( 'admin/jqadm/partial/pagination', 'common/partials/pagination' ),
            ['pageParams' => $params, 'pos' => 'top', 'total' => $this->get( 'total' ),
            'page' =>$this->session( 'aimeos/admin/jqadm/mypanel/page', [] )]
        );
    ?>

    <form class="list list-mypanel" method="POST" action="<?= $enc->attr( $this->url( $target, $controller, $action, $searchParams, [], $config ) ); ?>">
        <?= $this->csrf()->formfield(); ?>

        <table class="list-items table table-hover table-striped">

        <!-- table header -->

        <!-- table body -->

        </table>

        <?php if( $this->get( 'items', map() )->isEmpty() ) : ?>
            <div class="noitems"><?= $enc->html( sprintf( $this->translate( 'admin', 'No items found' ) ) ); ?></div>
        <?php endif; ?>
    </form>

    <?= $this->partial(
            $this->config( 'admin/jqadm/partial/pagination', 'common/partials/pagination' ),
            ['pageParams' => $params, 'pos' => 'bottom', 'total' => $this->get( 'total' ),
            'page' => $this->session( 'aimeos/admin/jqadm/mypanel/page', [] )]
        );
    ?>

</div>
<?php $this->block()->stop(); ?>
<?= $this->render( $this->config( 'admin/jqadm/template/page', 'common/page' ) ); ?>
```

There are a few things to keep care of:

vue-block
: The first `<div class="vue-block">` will initialize the Vue.js application, so Vue components will be rendered and functional

global search
: In the `<nav>` section, the global search box is rendered where editors can search for values in all fields offered by the manager. If you don't use managers to retrieve the data, you should remove that part.

pagination
: There's a top and bottom pagination included but the top pagination is only rendered if more items are available than shown. This decision is made in the partial itself.

content form
: The items returned by the JQAdm class are expected to be an `\Aimeos\Map` object, which wraps a list of items and offers a lot of helpful methods to work with the list of items. If you don't use managers, you have to change the lines calling Map methods.

block rendering
: There's a `$this->block()->start( 'jqadm_content' )` and `$this->block()->stop()` line as well as a call to `$this->render()`. Those lines will insert the list view into the page layout which includes the surrounding HTML.

## Table header

The table header renders the:

* link to delete all selected items
* columns for the item properties
* available actions like create, export, etc.
* column selector so editors can choose the shown columns

Use this partial as example, insert it instead of the `<!-- table header -->` marker in the base template and replace "Mypanel" and "mypanel" with your panel name (case sensitiv):

```php
<?php
    $newTarget = $this->config( 'admin/jqadm/url/create/target' );
    $newCntl = $this->config( 'admin/jqadm/url/create/controller', 'Jqadm' );
    $newAction = $this->config( 'admin/jqadm/url/create/action', 'create' );
    $newConfig = $this->config( 'admin/jqadm/url/create/config', [] );

    $delTarget = $this->config( 'admin/jqadm/url/delete/target' );
    $delCntl = $this->config( 'admin/jqadm/url/delete/controller', 'Jqadm' );
    $delAction = $this->config( 'admin/jqadm/url/delete/action', 'delete' );
    $delConfig = $this->config( 'admin/jqadm/url/delete/config', [] );

    $expTarget = $this->config( 'admin/jqadm/url/export/target' );
    $expCntl = $this->config( 'admin/jqadm/url/export/controller', 'Jqadm' );
    $expAction = $this->config( 'admin/jqadm/url/export/action', 'export' );
    $expConfig = $this->config( 'admin/jqadm/url/export/config', [] );

    $columnList = [
        'mypanel.id' => $this->translate( 'admin', 'ID' ),
        'mypanel.status' => $this->translate( 'admin', 'Status' ),
        'mypanel.label' => $this->translate( 'admin', 'Label' ),
        'mypanel.ctime' => $this->translate( 'admin', 'Created' ),
        'mypanel.mtime' => $this->translate( 'admin', 'Modified' ),
        'mypanel.editor' => $this->translate( 'admin', 'Editor' ),
    ];

    $default = $this->config( 'admin/jqadm/mypanel/fields', ['mypanel.id', 'mypanel.status', 'mypanel.label'] );
    $fields = $this->session( 'aimeos/admin/jqadm/mypanel/fields', $default );
?>
<thead class="list-header">
    <tr>
        <th class="select">
            <a class="btn act-delete fa" tabindex="1" data-multi="1"
                href="<?= $enc->attr( $this->url( $delTarget, $delCntl, $delAction, ['id' => ''] + $params, [], $delConfig ) ); ?>"
                title="<?= $enc->attr( $this->translate( 'admin', 'Delete this entry' ) ); ?>"
                aria-label="<?= $enc->attr( $this->translate( 'admin', 'Delete' ) ); ?>">
            </a>
        </th>

        <?= $this->partial(
                $this->config( 'admin/jqadm/partial/listhead', 'common/partials/listhead' ),
                ['fields' => $fields, 'params' => $params, 'data' => $columnList,
                'sort' => $this->session( 'aimeos/admin/jqadm/mypanel/sort', 'mypanel.id' )]
            );
        ?>

        <th class="actions">
            <div class="dropdown list-menu">
                <button class="btn act-menu fa" type="button" id="menuButton"
                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"
                    title="<?= $enc->attr( $this->translate( 'admin', 'Actions' ) ); ?>"
                    aria-label="<?= $enc->attr( $this->translate( 'admin', 'Actions' ) ); ?>"
                    tabindex="<?= $this->get( 'tabindex' ); ?>">
                </button>
                <ul class="dropdown-menu dropdown-menu-right" aria-labelledby="menuButton">
                    <li class="dropdown-item">
                        <a class="btn fa act-add" tabindex="1"
                            href="<?= $enc->attr( $this->url( $newTarget, $newCntl, $newAction, $params, [], $newConfig ) ); ?>"
                            title="<?= $enc->attr( $this->translate( 'admin', 'Insert new entry (Ctrl+I)' ) ); ?>"
                            aria-label="<?= $enc->attr( $this->translate( 'admin', 'Add' ) ); ?>">
                        </a>
                    </li>
                    <li class="dropdown-item">
                        <a class="btn fa act-download" tabindex="1"
                            href="<?= $enc->attr( $this->url( $expTarget, $expCntl, $expAction, $params, ['queue' => 'mypanel-export'], $expConfig ) ); ?>"
                            aria-label="<?= $enc->attr( $this->translate( 'admin/ext', 'Export' ) ); ?>"
                            title="<?= $enc->attr( $this->translate( 'admin/ext', 'Export' ) ); ?>">
                            <?= $enc->html( $this->translate( 'admin/ext', 'Export' ) ); ?>
                        </a>
                    </li>
                </ul>
            </div>

            <?= $this->partial(
                    $this->config( 'admin/jqadm/partial/columns', 'common/partials/columns' ),
                    ['fields' => $fields, 'data' => $columnList]
                );
            ?>
        </th>
    </tr>
</thead>
```

Notes for the table header of the list view:

mass action
: The first column is for performing mass actions like deleting several items at once. If you don't want or support that, you can leave that column out.

data columns
: All columns related to item properties are rendered by the *listhead* partial. For that, it uses the columns in `$fields` that are read from the session if the editor changed the columns (from configuration otherwise). The column for the default sorting must be passed and sorting is activated for all columns. If you don't want that, you have to pass *NULL* as value in `$columnList` for that column.

action drop-down
: You can add several actions to `<th class="actions">` and should provide at least a "create" action if applicable.

column selector
: The *columns* partial will render the drop down for the column selection based on the list of available columns (`$columnList`) and the shown ones (`$fields`).

## Table body

The table header renders the

* filter toolbar for each column
* one row for each item
* item actions

You can adapt this partial to your needs, insert it instead of the `<!-- table body -->` marker in the base template and replace "Mypanel" and "mypanel" with your panel name (case sensitiv):

```php
<?php
    $getTarget = $this->config( 'admin/jqadm/url/get/target' );
    $getCntl = $this->config( 'admin/jqadm/url/get/controller', 'Jqadm' );
    $getAction = $this->config( 'admin/jqadm/url/get/action', 'get' );
    $getConfig = $this->config( 'admin/jqadm/url/get/config', [] );

    $copyTarget = $this->config( 'admin/jqadm/url/copy/target' );
    $copyCntl = $this->config( 'admin/jqadm/url/copy/controller', 'Jqadm' );
    $copyAction = $this->config( 'admin/jqadm/url/copy/action', 'copy' );
    $copyConfig = $this->config( 'admin/jqadm/url/copy/config', [] );

    $delTarget = $this->config( 'admin/jqadm/url/delete/target' );
    $delCntl = $this->config( 'admin/jqadm/url/delete/controller', 'Jqadm' );
    $delAction = $this->config( 'admin/jqadm/url/delete/action', 'delete' );
    $delConfig = $this->config( 'admin/jqadm/url/delete/config', [] );

    $default = $this->config( 'admin/jqadm/mypanel/fields', ['mypanel.id', 'mypanel.status', 'mypanel.label'] );
    $fields = $this->session( 'aimeos/admin/jqadm/mypanel/fields', $default );
?>
<tbody>
    <?= $this->partial(
        $this->config( 'admin/jqadm/partial/listsearch', 'common/partials/listsearch' ), [
            'fields' => array_merge( $fields, ['select'] ),
            'filter' => $this->session( 'aimeos/admin/jqadm/mypanel/filter', [] ),
            'data' => [
                'select' => ['type' => 'checkbox'],
                'mypanel.id' => ['op' => '=='],
                'mypanel.status' => ['op' => '==', 'type' => 'select', 'val' => [
                    '1' => $this->translate( 'mshop/code', 'status:1' ),
                    '0' => $this->translate( 'mshop/code', 'status:0' ),
                    '-1' => $this->translate( 'mshop/code', 'status:-1' ),
                    '-2' => $this->translate( 'mshop/code', 'status:-2' ),
                ]],
                'mypanel.label' => [],
                'mypanel.ctime' => ['op' => '-', 'type' => 'datetime-local'],
                'mypanel.mtime' => ['op' => '-', 'type' => 'datetime-local'],
                'mypanel.editor' => [],
            ]
        ] );
    ?>

    <?php foreach( $this->get( 'items', [] ) as $id => $item ) : ?>
        <?php $url = $enc->attr( $this->url( $getTarget, $getCntl, $getAction, ['id' => $id] + $params, [], $getConfig ) ) ?>
        <tr class="list-item <?= $this->site()->readonly( $item->getSiteId() ); ?>"
            data-label="<?= $enc->attr( $item->getLabel() ) ?>">
            <td class="select">
                <input class="form-control" type="checkbox" tabindex="1"
                    name="<?= $enc->attr( $this->formparam( ['id', ''] ) ) ?>"
                    value="<?= $enc->attr( $item->getId() ) ?>" />
            </td>
            <?php if( in_array( 'mypanel.id', $fields ) ) : ?>
                <td class="mypanel-id">
                    <a class="items-field" href="<?= $url; ?>" tabindex="1">
                        <?= $enc->html( $item->getId() ); ?>
                    </a>
                </td>
            <?php endif; ?>
            <?php if( in_array( 'mypanel.status', $fields ) ) : ?>
                <td class="mypanel-status">
                    <a class="items-field" href="<?= $url; ?>">
                        <div class="fa status-<?= $enc->attr( $item->getStatus() ); ?>"></div>
                    </a>
                </td>
            <?php endif; ?>
            <?php if( in_array( 'mypanel.label', $fields ) ) : ?>
                <td class="mypanel-label">
                    <a class="items-field" href="<?= $url; ?>">
                        <?= $enc->html( $item->getLabel() ); ?>
                    </a>
                </td>
            <?php endif; ?>
            <?php if( in_array( 'mypanel.ctime', $fields ) ) : ?>
                <td class="mypanel-ctime">
                    <a class="items-field" href="<?= $url; ?>">
                        <?= $enc->html( $item->getTimeCreated() ); ?>
                    </a>
                </td>
            <?php endif; ?>
            <?php if( in_array( 'mypanel.mtime', $fields ) ) : ?>
                <td class="mypanel-mtime">
                    <a class="items-field" href="<?= $url; ?>">
                        <?= $enc->html( $item->getTimeModified() ); ?>
                    </a>
                </td>
            <?php endif; ?>
            <?php if( in_array( 'mypanel.editor', $fields ) ) : ?>
                <td class="mypanel-editor">
                    <a class="items-field" href="<?= $url; ?>">
                        <?= $enc->html( $item->getEditor() ); ?>
                    </a>
                </td>
            <?php endif; ?>

            <td class="actions">
            <a class="btn act-copy fa" tabindex="1"
                    href="<?= $enc->attr( $this->url( $copyTarget, $copyCntl, $copyAction, ['id' => $id] + $params, [], $copyConfig ) ); ?>"
                    title="<?= $enc->attr( $this->translate( 'admin', 'Copy this entry' ) ); ?>"
                    aria-label="<?= $enc->attr( $this->translate( 'admin', 'Copy' ) ); ?>">
                </a>
                <?php if( !$this->site()->readonly( $item->getSiteId() ) ) : ?>
                    <a class="btn act-delete fa" tabindex="1"
                        href="<?= $enc->attr( $this->url( $delTarget, $delCntl, $delAction, ['resource' => 'mypanel', 'id' => $id] + $params, [], $delConfig ) ); ?>"
                        title="<?= $enc->attr( $this->translate( 'admin', 'Delete this entry' ) ); ?>"
                        aria-label="<?= $enc->attr( $this->translate( 'admin', 'Delete' ) ); ?>">
                    </a>
                <?php endif; ?>
            </td>
        </tr>
    <?php endforeach; ?>
</tbody>
```

Notes for the table header of the list view:

search filter
: The *listsearch* partial will create the search filter for the whole table. Thus, you have to add the first column for the mass action and the stored filter of the last search for populating the filters again. The *data* property must contain a list of the search keys (e.g. "mycolumn.id) and hints for building the filter. Available filter hints are:

* type : "select", "checkbox" or any valid type for input fields (default: "text")
* op : filter operator, i.e. '==', '!=', '<', '<=', '>', '>=' or '-' (range operator for date/time fields)
* val : options for the select box with expected value as key and translated label as value

If an empty array without any hint is passed, an `<input type="text">` is rendered and the value entered is compared for equality (`==`).

table rows
: The columns in the rows are rendered depending on the `$fields` content and linked so the detail view opens when the editor clicks on a row.

actions
: For each row, offering one or more action is possible at the end. By default, copying and deleting an item should be offered if applicable

# Detail template

The details template for a panel must be stored in your own Aimeos extension in `./templates/admin/jqadm/<panel name>/item.php` and consists of the:

* navigation bar including Save/Cancel buttons
* left sidebar with sub-panels
* form with content elements

Use this as base template for your own one and replace "Mypanel" and "mypanel" with your panel name (case sensitiv):

```php
<?php
    $enc = $this->encoder();
    $params = $this->get( 'pageParams', [] );

    $target = $this->config( 'admin/jqadm/url/save/target' );
    $cntl = $this->config( 'admin/jqadm/url/save/controller', 'Jqadm' );
    $action = $this->config( 'admin/jqadm/url/save/action', 'save' );
    $config = $this->config( 'admin/jqadm/url/save/config', [] );
?>
<?php $this->block()->start( 'jqadm_content' ); ?>

<form class="item item-mypanel form-horizontal" method="POST" enctype="multipart/form-data"
    action="<?= $enc->attr( $this->url( $target, $cntl, $action, $params, [], $config ) ); ?>">

    <input id="item-id" type="hidden"
        name="<?= $enc->attr( $this->formparam( ['item', 'mypanel.id'] ) ); ?>"
        value="<?= $enc->attr( $this->get( 'itemData/mypanel.id' ) ); ?>" />
    <input id="item-next" type="hidden"
        name="<?= $enc->attr( $this->formparam( ['next'] ) ); ?>" value="get" />

    <?= $this->csrf()->formfield(); ?>

    <nav class="main-navbar">
        <h1 class="navbar-brand">
            <span class="navbar-title">
                <?= $enc->html( $this->translate( 'admin', 'Mypanel' ) ); ?>
            </span>
            <span class="navbar-id">
                <?= $enc->html( $this->get( 'itemData/mypanel.id' ) ); ?>
            </span>
            <span class="navbar-label">
                <?= $enc->html( $this->get( 'itemData/mypanel.label' ) ?: $this->translate( 'admin', 'New' ) ); ?>
            </span>
            <span class="navbar-site">
                <?= $enc->html( $this->site()->match( $this->get( 'itemData/mypanel.siteid' ) ) ); ?>
            </span>
        </h1>
        <div class="item-actions">
            <?= $this->partial( $this->config( 'admin/jqadm/partial/itemactions', 'common/partials/itemactions' ), ['params' => $params] ); ?>
        </div>
    </nav>
    <div class="row item-container">
        <div class="col-md-3 item-navbar">

            <!-- navigation sidebar -->

        </div>
        <div class="col-md-9 item-content tab-content">

            <!-- tab content -->

            <?= $this->get( 'itemBody' ); ?>
        </div>
        <div class="item-actions">
            <?= $this->partial( $this->config( 'admin/jqadm/partial/itemactions', 'common/partials/itemactions' ), ['params' => $params] ); ?>
        </div>
    </div>
</form>
<?php $this->block()->stop(); ?>
<?= $this->render( $this->config( 'admin/jqadm/template/page', 'common/page' ) ); ?>
```

Notes for the detail template:

form
: The form must enclose the complete content so ever input field in the detail view will be sent to the server when the editor clicks on "Save"

hidden input fields
: They are important because they contain the ID of the item and the next action parameter

CSRF protection
: The `<?= $this->csrf()->formfield(); ?>` is very important because it will contain the token to protect against client side request forgery. If you leave that out, frameworks supporting CSRF protection will refuse your request

item action
: This partial will be rendered twice, one in the header and one below the content but the last one is only shown on mobile devices. It will create the "Cancel" and "Save" button including options like "Save & Close", "Save & Copy" and "Save & New"

## Sidebar

The navigation sidebar for the sub-parts renders the:

* list of tabs for the sub-parts
* meta data (mtime, ctime, editor)

You can adapt this partial to your needs, insert it instead of the `<!-- navigation sidebar -->` marker in the base template and replace "Mypanel" and "mypanel" with your panel name (case sensitiv):

```php
<div class="navbar-content">
    <ul class="nav nav-tabs flex-md-column flex-wrap d-flex justify-content-between" role="tablist">
        <li class="nav-item basic">
            <a class="nav-link active" href="#basic" data-toggle="tab" role="tab" aria-expanded="true" aria-controls="basic">
                <?= $enc->html( $this->translate( 'admin', 'Basic' ) ); ?>
            </a>
        </li>
        <?php foreach( array_values( $this->get( 'itemSubparts', [] ) ) as $idx => $subpart ) : ?>
            <li class="nav-item <?= $enc->attr( $subpart ); ?>">
                <a class="nav-link" href="#<?= $enc->attr( $subpart ); ?>" data-toggle="tab" role="tab" tabindex="<?= ++$idx + 1; ?>">
                    <?= $enc->html( $this->translate( 'admin', $subpart ) ); ?>
                </a>
            </li>
        <?php endforeach; ?>
    </ul>
    <div class="item-meta text-muted">
        <small>
            <?= $enc->html( $this->translate( 'admin', 'Modified' ) ); ?>:
            <span class="meta-value"><?= $enc->html( $this->get( 'itemData/mypanel.mtime' ) ); ?></span>
        </small>
        <small>
            <?= $enc->html( $this->translate( 'admin', 'Created' ) ); ?>:
            <span class="meta-value"><?= $enc->html( $this->get( 'itemData/mypanel.ctime' ) ); ?></span>
        </small>
        <small>
            <?= $enc->html( $this->translate( 'admin', 'Editor' ) ); ?>:
            <span class="meta-value"><?= $enc->html( $this->get( 'itemData/mypanel.editor' ) ); ?></span>
        </small>
    </div>
</div>
```

Notes for the sidebar navigation:

tabindex
: The sitebar tabs including the content behind that tabs gets their own tabindex so editors can use the tab key to move the focus not only to the next input field but also to the next sub-part.

## Basic tab

The content in the basic tab usually consists of input and select fields that contains the data of the item that should be managed by the editor. It's basic HTML with [Bootstrap](https://getbootstrap.com) styles but can also contain [Vue.js](https://vuejs.org) components:

```php
<div id="basic" class="row item-basic tab-pane fade show active" role="tabpanel" aria-labelledby="basic">

    <div class="col-xl-6 content-block vue-block <?= $this->site()->readonly( $this->get( 'itemData/mypanel.siteid' ) ); ?>"
        data-data="<?= $enc->attr( $this->get( 'itemData', new stdClass() ) ) ?>">

        <div class="form-group row mandatory">
            <label class="col-sm-4 form-control-label"><?= $enc->html( $this->translate( 'admin', 'Status' ) ); ?></label>
            <div class="col-sm-8">
                <select class="form-control custom-select item-status" required="required" tabindex="1"
                    name="<?= $enc->attr( $this->formparam( ['item', 'mypanel.status'] ) ); ?>"
                    <?= $this->site()->readonly( $this->get( 'itemData/mypanel.siteid' ) ); ?> >
                    <option value="">
                        <?= $enc->html( $this->translate( 'admin', 'Please select' ) ); ?>
                    </option>
                    <option value="1" <?= $selected( $this->get( 'itemData/mypanel.status', 1 ), 1 ); ?> >
                        <?= $enc->html( $this->translate( 'mshop/code', 'status:1' ) ); ?>
                    </option>
                    <option value="0" <?= $selected( $this->get( 'itemData/mypanel.status', 1 ), 0 ); ?> >
                        <?= $enc->html( $this->translate( 'mshop/code', 'status:0' ) ); ?>
                    </option>
                    <option value="-1" <?= $selected( $this->get( 'itemData/mypanel.status', 1 ), -1 ); ?> >
                        <?= $enc->html( $this->translate( 'mshop/code', 'status:-1' ) ); ?>
                    </option>
                    <option value="-2" <?= $selected( $this->get( 'itemData/mypanel.status', 1 ), -2 ); ?> >
                        <?= $enc->html( $this->translate( 'mshop/code', 'status:-2' ) ); ?>
                    </option>
                </select>
            </div>
        </div>
        <?php if( ( $types = $this->get( 'itemTypes', map() )->col( 'mypanel.type.label', 'mypanel.type.code' ) )->count() !== 1 ) : ?>
            <div class="form-group row mandatory">
                <label class="col-sm-4 form-control-label"><?= $enc->html( $this->translate( 'admin', 'Type' ) ); ?></label>
                <div class="col-sm-8">
                    <select is="select-component" class="form-control custom-select item-type" required v-bind:tabindex="'1'"
                        v-bind:readonly="'<?= $this->site()->readonly( $this->get( 'itemData/mypanel.siteid' ) ); ?>' ? true : false"
                        v-bind:name="'<?= $enc->attr( $this->formparam( ['item', 'mypanel.type'] ) ); ?>'"
                        v-bind:text="'<?= $enc->html( $this->translate( 'admin', 'Please select' ) ); ?>'"
                        v-bind:items="JSON.parse('<?= $enc->attr( $types->toArray() ) ?>')"
                        v-model="data['mypanel.type']" >
                        <option value="<?= $enc->attr( $this->get( 'itemData/mypanel.type' ) ) ?>">
                            <?= $enc->html( $types[$this->get( 'itemData/mypanel.type', '' )] ?? $this->translate( 'admin', 'Please select' ) ) ?>
                        </option>
                    </select>
                </div>
            </div>
        <?php else : ?>
            <input class="item-type" type="hidden"
                name="<?= $enc->attr( $this->formparam( ['item', 'mypanel.type'] ) ); ?>"
                value="<?= $enc->attr( $types->firstKey() ) ?>" />
        <?php endif; ?>
        <div class="form-group row mandatory">
            <label class="col-sm-4 form-control-label help"><?= $enc->html( $this->translate( 'admin', 'Label' ) ); ?></label>
            <div class="col-sm-8">
                <input class="form-control item-label" type="text" required="required" tabindex="1"
                    name="<?= $this->formparam( ['item', 'mypanel.label'] ); ?>"
                    placeholder="<?= $enc->attr( $this->translate( 'admin', 'Internal name (required)' ) ); ?>"
                    value="<?= $enc->attr( $this->get( 'itemData/mypanel.label' ) ); ?>"
                    <?= $this->site()->readonly( $this->get( 'itemData/mypanel.siteid' ) ); ?> />
            </div>
            <div class="col-sm-12 form-text text-muted help-text">
                <?= $enc->html( $this->translate( 'admin', 'Internal article name, will be used on the web site and for searching only if no other mypanel names in any language exist' ) ); ?>
            </div>
        </div>
        <div class="form-group row optional advanced">
            <label class="col-sm-4 form-control-label help"><?= $enc->html( $this->translate( 'admin', 'Created' ) ); ?></label>
            <div class="col-sm-8">
                <input is="flat-pickr" class="form-control item-ctime" type="datetime-local" tabindex="1"
                    name="<?= $enc->attr( $this->formparam( ['item', 'mypanel.ctime'] ) ); ?>"
                    placeholder="<?= $enc->attr( $this->translate( 'admin', 'YYYY-MM-DD hh:mm:ss (optional)' ) ); ?>"
                    v-bind:value="'<?= $enc->attr( $this->datetime( $this->get( 'itemData/mypanel.ctime' ) ) ); ?>'"
                    v-bind:disabled="'<?= $this->site()->readonly( $this->get( 'itemData/mypanel.siteid' ) ); ?>' !== ''"
                    v-bind:config="Aimeos.flatpickr.datetime" />
            </div>
            <div class="col-sm-12 form-text text-muted help-text">
                <?= $enc->html( $this->translate( 'admin', 'Since when the mypanel is available, used for sorting in the front-end' ) ); ?>
            </div>
        </div>
    </div><!--

    --><div class="col-xl-6 content-block vue-block <?= $this->site()->readonly( $this->get( 'itemData/mypanel.siteid' ) ); ?>"
        data-data="<?= $enc->attr( $this->get( 'itemData', new stdClass() ) ) ?>">

    </div>
</div>
```

Notes for the basic tab content:

tab pane
: The first `<div>` is for the Boostrap tab and must not be the root of the Vue.js application

vue block
: In the second `<div>`, the Vue applcation is initialized because it contains the `vue-block` class. The Aimeos JS creates a Vue instance for each HTML node that contains the class. You can add arbitrary data to the Vue instance in the `data-data="..."` attribute, which must contain a valid Javascript object (`{}`).

!!! warning
    There can be more than one `vue-block` class for different columns or sub-parts but it's not allowed to have nested Vue instances. Use [Vue components](https://vuejs.org/v2/guide/components.html) instead and pass required data as props.

The example for the basic tab also contains the most often used input types:

input
: Most of the used fields are standard input fields with different values for the *type* attribute depending on the required values

select (standard)
: The standard HTML select tag for the item status is straight forward

select (Vue component)
: There's an alternative select implemented as Vue.js component that is able to show options dynamically. It also adds the initial value as options to the select list if it doesn't exist in the list of given options. Also, the type field example is only shown if there's more than one option available due to the if/else

date picker
: In case of input fields with type `datetime-local`, you can also use the *flatpickr* Vue component because e.g. Safari doesn't support date/time fields at all and doesn't offer a calendar widget

There are also [Vue.js components](https://github.com/aimeos/ai-admin-jqadm/blob/master/admin/jqadm/themes/vue-components.js) available for:

* auto completes
* combo boxes
* config tables
* HTML editors
* property tables
* tax rate fields

Furthermore, the JQAdm code contains complete components for manging:

* [addresses](https://github.com/aimeos/ai-admin-jqadm/blob/master/templates/admin/jqadm/customer/item-address.php)
* [images/media](https://github.com/aimeos/ai-admin-jqadm/blob/master/templates/admin/jqadm/product/item-media.php)
* [prices](https://github.com/aimeos/ai-admin-jqadm/blob/master/templates/admin/jqadm/product/item-price.php)
* [texts](https://github.com/aimeos/ai-admin-jqadm/blob/master/templates/admin/jqadm/product/item-text.php)

They consist of [Vue.js code](https://github.com/aimeos/ai-admin-jqadm/blob/master/admin/jqadm/themes/admin-aux.js) and HTML inline templates.
