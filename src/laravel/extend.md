# Adapt pages

When talking about pages we tend to think of the full HTML response that is sent to the visitor's browser after they enter a [shop URL](http://laravel.demo.aimeos.org/default/en/EUR). It includes the output from the Aimeos components embedded into the [base template](https://github.com/aimeos/aimeos-laravel#setup) you've provided after installation.

This article focuses on changing the components that are visible on a page. If you want to adapt only the layout, please read the article about [theming of the shop components](../frontend/html/theme-basics.md).

All Aimeos pages can contain a list of pre-defined sections:

* **aimeos_styles** ( additional CSS files)
* **aimeos_scripts** (additional JS files)
* **aimeos_header** (HTML head tags like product title and meta information)
* **aimeos_head** (head section including the small basket for example)
* **aimeos_nav** (shop navigation and faceted search)
* **aimeos_stage** (stage area including breadcrumb navigation)
* **aimeos_body** (main content for product lists, details or the checkout process)
* **aimeos_aside** (user related content, e.g. last seen products)

The templates used by the controller actions decides if there's some content inside these sections. You can find these templates in the [src/views](https://github.com/aimeos/aimeos-laravel/tree/master/src/views) directory and its sub-directories of the Aimeos e-commerce package.

## Don't change the package

Even if it might seem the easiest way to modify the templates and configuration files directly in the Aimeos e-commerce package, it's really a bad idea! You will lose the ability to update the Aimeos package. If you were to make a package update, all of the changes you had made to the core package would be reset to the standard configuration and templates.

Instead, Laravel provides a convenient way to overwrite the configuration files as well as the templates for any package. To **overwrite the configuration**, you only have to modify the configuration settings in the **config/shop.php** file of your Laravel application:

```php
'page' => [
    'account-index' => ['account/history']
]
```

This would overwrite the list of components for the "MyAccount" page from the Aimeos package.

Another way you can adapt specific pages is by **rewriting existing templates** from the `vendor/aimeos/aimeos-laravel/src/views` directory. These templates can be overwritten by creating your own copies of these files into your Laravel application's `resources/views/vendor/shop` directory and sub-directories. These copies will overwrite the Aimeos vendor package's views.

As stated in Laravel's documentation about [overriding package views](https://laravel.com/docs/master/packages#views), "When you use the loadViewsFrom method (inside of your service provider's boot method), Laravel actually registers two locations for your views: the application's `resources/views/vendor/` directory and the directory you specify."

## Reorder components

The easiest possibility is changing the order of the single components inside the pre-defined sections. Let's use the page template for the account page as example:

```php
@extends('shop::base')

@section('aimeos_header')
    <?= $aiheader['basket/mini'] ?>
    <?= $aiheader['account/history'] ?>
    <?= $aiheader['account/favorite'] ?>
    <?= $aiheader['account/watch'] ?>
    <?= $aiheader['catalog/session'] ?>
@stop

@section('aimeos_head')
    <?= $aibody['basket/mini'] ?>
@stop

@section('aimeos_body')
    <?= $aibody['account/history'] ?>
    <?= $aibody['account/favorite'] ?>
    <?= $aibody['account/watch'] ?>
@stop

@section('aimeos_aside')
    <?= $aibody['catalog/session'] ?>
@stop
```

The `@extends('shop::base')` instruction defines the template this one will inherit the rest of the layout from. To change the order of the components in the `@section('aimeos_body')`, you can simple reorder the single lines between the `@section('...') ... @stop` tags, e.g:

```php
@section('aimeos_body')
    <?= $aibody['account/favorite'] ?>
    <?= $aibody['account/watch'] ?>
    <?= $aibody['account/history'] ?>
@stop
```

This would move the order history component to the end of the body container in the HTML response.

## Add components

Adding more components to an existing page consists of two steps:

* Add the component name to the modified page configuration
* Insert the body and header output in the page template

By default, not all shop components are available on every page as this would create a lot of unnecessary load on your server. Instead, only the components that are rendered, which are configured in the "page" section of the `./config/shop.php` file, are handed over to the template file. e.g.

```php
'page' => [
    'account' => [
		'account/history','account/favorite','account/watch',
		'basket/mini','catalog/session'
	]
]
```

Available components are listed for each controller action and they are identified using the [directory structure](https://github.com/aimeos/ai-client-html/tree/master/client/html/src/Client/Html) of the HTML clients in the core.

Thus, the account history component in the "Client/Html/Account/History" directory is addressed via the string "account/history". Similarly, the product listing component is identified by "catalog/list" and the product detail component is identified by "catalog/detail". This works for all components besides the ones that are in the "Client/Html/Common" and "Client/Html/Email" directory.

!!! warning
    Please keep in mind that some components need specific parameters like the "catalog/detail" component, which requires at least a value for the "d_prodid" parameter. There's a [[Developers/Html_frontend/Used_parameter_names|complete list of parameters used]] available for reference.

For example, if you want to add the catalog filter component to your "MyAccount" page as well, you can add its name inside the configuration array of the page component list:

```php
'page' => [
    'account-index' => [
		'account/history','account/favorite','account/watch',
		'basket/mini','catalog/session','catalog/filter'
	]
]
```

The order of the component names does not matter. The header and body of the catalog filter component will now be available to use inside the `aibody` and `aiheader` array variables in the template file specified in the "account" controller / "index" action. Nevertheless, there's no output yet because you need to tell the template where their content should be rendered to:

```php
@section('aimeos_header')
    ....
    <?= $aiheader['catalog/filter'] ?>
@stop

@section('aimeos_nav')
    <?= $aibody['catalog/filter'] ?>
@stop
```

For the body, we use the "aimeos_nav" block so the filter menu will be located in the same place like in the other pages but you are free to put it in every block you want except the "aimeos_header" block.

Contrary to that, the header data must always be placed in the "aimeos_header" block to be effective but the order inside the "aimeos_header" block is most of the time not important. Both lines must be printed directly with the "<?= ... ?>" tags to avoid the HTML being escaped by the Blade template engine.

## Remove components

Removing components is simple as you only have to provide a page template without the aibody and aiheader lines of the component, e.g.:

```php
@extends('shop::base')

@section('aimeos_header')
    <?= $aiheader['basket/mini'] ?>
    <?= $aiheader['account/history'] ?>
    <?= $aiheader['account/favorite'] ?>
    <?= $aiheader['account/watch'] ?>
@stop

@section('aimeos_head')
    <?= $aibody['basket/mini'] ?>
@stop

@section('aimeos_body')
    <?= $aibody['account/history'] ?>
    <?= $aibody['account/favorite'] ?>
    <?= $aibody['account/watch'] ?>
@stop
```

That template wouldn't output the "catalog/session" body and header HTML but to avoid rending them at all, you need to overwrite the page configuration as well:

```php
'page' => [
    'account-index' => [
		'account/history','account/favorite','account/watch','basket/mini'
	]
]
```

!!! tip
    For testing, it's OK to remove only the lines from the page templates but you get significant speedups in your production environment by providing a modified page configuration too.

# Create pages

The Aimeos package contains all pages necessary to create a complete web shop. Sometimes you might want to add additional pages that should contain Aimeos shop components.

On your new page, you might want components like the small basket or the list of last seen products from the catalog session component. If you only want to modify the output of existing pages, please take a look at the article about [adapting pages](#adapt-pages) instead.

Assuming that you've already created a controller, a controller action, and a template for your new page (if not, take a look into the "Basics" section of the [Laravel documentation](https://laravel.com/docs/master) this article contains the required steps to add the Aimeos components to your page.

## Adapt your controller

The easiest and most efficient way to retrieve the body and header parts from Aimeos components is to use the "Shop" facade and call the `get()` method inside your controller action:

```php
namespace App\Http\Controllers;

use Aimeos\Shop\Facades\Shop;

class ExampleController extends Controller
{
    public function indexAction()
    {
        foreach( config( 'shop.page.mypage' ) as $name )
        {
            $params['aiheader'][$name] = Shop::get( $name )->getHeader();
            $params['aibody'][$name] = Shop::get( $name )->getBody();
        }
        // do some more stuff
        return \View::make('mypagetmpl', $params);
    }
}
```

The result of the first line of this method will be an array with keys for "aibody" and "aiheader" that contain the associative arrays of the component names and the rendered HTML. e.g.

```php
$ouput = [
    'aibody' => [
        'basket/mini' => '<div> ... rendered HTML ... ',
        'catalog/session' => '<div> ... rendered HTML ... '
    ],
    'aiheader' => [
        'basket/mini' => '... HTML head tags ...',
        'catalog/session' => '... HTML head tags ...'
	],
);
```

This array is then passed to the `\View::make()` method so the "aibody" and "aiheader" variables will be available in the template.

## Configure the components

Up to now, there would be no data in the aibody and aiheader arrays because you haven't defined that one or more components should be available. This is done in the `config/shop.php` file of your Laravel application. The parameter you passed to the `get()` method call in your controller will be used as the required configuration key. In this example we have used "mypage":

```php
'page' => [
    'mypage' => ['basket/mini','catalog/session']
]
```

Now you have told your controller action that the method using the "mypage" parameter (which in this case is the get() method) should render the body and header output for the "basket/mini" and the "catalog/session" components.

Available components are identified using the [directory structure](https://github.com/aimeos/ai-client-html/tree/master/client/html/src/Client/Html) of the HTML clients.

Thus, the catalog session component in the "Client/Html/Catalog/Session" directory is addressed via the string "catalog/session". Similarly, the product listing component is identified by "catalog/list", and the product detail component is identified by "catalog/detail". This works for all components besides the ones that are in the "Client/Html/Common" and "Client/Html/Email" directory.

!!! warning
    Please keep in mind that some components need specific parameters like the "catalog/detail" component, which requires at least a value for the "d_prodid" parameter. There's a [complete list of parameters used](../frontend/html/parameter-names.md) available for reference.

## Modify your template

After adding the configuration, there are two variables available in your template containing arrays: "aibody" and "aiheader". They store the rendered HTML that should now be displayed somewhere in your template which can contain these blocks:

```php
@extends('shop::base')

@section('aimeos_styles')
@stop

@section('aimeos_scripts')
@stop

@section('aimeos_header')
@stop

@section('aimeos_head')
@stop

@section('aimeos_nav')
@stop

@section('aimeos_stage')
@stop

@section('aimeos_body')
@stop

@section('aimeos_aside')
@stop
```

You must extend your template from the base template of the Aimeos shop package. If not extended, the base CSS and Javascript files will be missing and no styling will be applied. There is no client side code available for the full functionality.

The single blocks correspond to the blocks of your [root layout template](https://github.com/aimeos/aimeos-laravel#setup) which you created after installation. Depending on where you want to display the output, you have to insert the necessary lines into the corresponding block. For example:

```php
@section('aimeos_header')
    <?= $aiheader['basket/mini'] ?>
    <?= $aiheader['catalog/session'] ?>
@stop

@section('aimeos_head')
    <?= $aibody['basket/mini'] ?>
@stop

@section('aimeos_aside')
     <?= $aibody['catalog/session'] ?>
@stop
```

We have chosen the "aimeos_head" block for placement of the basket mini-body (`aibody['basket/mini']`). The mini-basket will be positioned in the same place as it appears on the other shop pages. You are free to put it in every block you want except the "aimeos_header" block, which instead contains `aiheader['basket/mini']`.

The header data must always be placed in the "aimeos_header" block to be effective. Both lines within the header data must be printed directly using the `<?= ... ?>` tags to avoid the HTML being escaped by the Blade template engine. The order inside the "aimeos_header" block is usually not important.

The same rules apply to the catalog session-body (`aibody['catalog/session']`). In our example we have chosen to place the catalog session-body in the "aimeos_aside" block.

If there are empty blocks after you've added all the output, you can remove them safely.

# Custom routes

Routes are defined in the `src/routes.php` of the Aimeos shop package and a set of standard routes is provided by default. Each route has at least a name, a corresponding path, and a `controller@action` part:

```php
Route::match( ['GET', 'POST' ] '<path of the route>', [
	'as' => '<route name>',
	'uses' => 'Aimeos\Shop\Controller\<controller name>@<action name>'
));
```

Each route creates links to one page of your application. The route names are important for the core library because the Laravel router needs their names for generating the correct routes for a given parameter.

## Route names

The names of the standard routes are predefined in the [routes.php](https://github.com/aimeos/aimeos-laravel/blob/master/src/routes.php) file. Besides the "admin" routes, which are not listed, their names are:

* **aimeos_shop_account** ("my account" page for each user)
* **aimeos_shop_account_download** (file downloads for virtual products)
* **aimeos_shop_account_favorite** (favorite products in "my account")
* **aimeos_shop_account_watch** (watched products in "my account")
* **aimeos_shop_basket** (standalone basket page)
* **aimeos_shop_count** (product counts for the faceted search in JSON format)
* **aimeos_shop_detail** (product detail page)
* **aimeos_shop_list** (product list page)
* **aimeos_shop_session_pinned** (pinned products in customer session)
* **aimeos_shop_suggest** (list of products for search suggestions in JSON format)
* **aimeos_shop_stock** (product stock information in JSON format)
* **aimeos_shop_checkout** (standalone checkout process page)
* **aimeos_shop_confirm** ("thank you" page after completing the order)
* **aimeos_shop_update** (payment update notifications)
* **aimeos_shop_terms** (terms and conditions page)
* **aimeos_shop_privacy** (privacy policy page)

They are split into several route groups. Each of these route groups can be configured separately in the "routes" array of your `config/shop.php`.

## Adapt existing routes

For all existing routes, you can change the path and the default parameters by redefining the routes in your `routes/web.php` file using the same name. For example, to change the path of the "aimeos_shop_terms" to "/terms_and_conditions", you only need to create a route with that path in the routes.php file:

```php
Route::get('terms_and_conditions', [
	'as' => 'aimeos_shop_terms',
	'uses' => '\Aimeos\Shop\Controller\PageController@termsAction'
));
```

Similarly, changing the controller and action name to a custom one ("MyController" and "mytermsAction") implemented in your application is done by adapting the "uses" value in the second parameter of the route:

```php
Route::get('terms', [
	'as' => 'aimeos_shop_terms',
	'uses' => 'MyController@mytermsAction'
));
```

In this case, your controller must be placed in the `./app/Http/Controllers` directory. More details can be found in the [Laravel routing documentation](https://laravel.com/docs/master/routing).

## Routes for multiple sites, languages and currencies

Aimeos is able to manage many sites in one installation with different languages and currencies for each site. If you have a setup with at least two sites, languages, or currencies, you need to adapt the values of the "admin", "account" or "default" settings in the "routes" array of your `config/shop.php`:

```php
'routes' => [
	'account' => ['prefix' => '{site}/{locale}/{currency}', ...],
	'default' => ['prefix' => '{site}/{locale}/{currency}', ...]
);
```

The value for the "prefix" key can be used to add a fixed prefix string (like `/shop`) and can also be changed to support these placeholders for the route definition:

* **{site}** (unique site code from "code" field in the "mshop_locale_site" table)
* **{locale}** (language ID from the "langid" field in the "mshop_locale" table)
* **{currency}** (currency ID from the "currencyid" field in the "mshop_locale" table)

You can reorder the placeholders the way you like such as moving the `{locale}` placeholder to the front. If your shop does not use more than one site, language, or currency, you can leave those placeholders out. The Aimeos shop will automatically use the default values in this case.

The "site" parameter is always "default" and the language and currency parameters are the ones defined in the "Locale" tab of the administration interface.

!!! warning
    You cannot add the "site", "locale", and "currency" placeholders to the "admin" routes of the Aimeos package. At least the "site" placeholder is already part of that route and using the same placeholder twice in one route will fail.

## Add new routes

If you've implemented a new Aimeos core component that generates URLs to a new page you must add a new custom route. The route name can be chosen but for clarity, you should prefix it with "aimeos_shop_", e.g.

```php
Route::get('new_page', [
	'as' => 'aimeos_shop_mypage',
	'uses' => 'MyController@myAction'
));
```

The Aimeos core component will need to know the name of the new route. It's then handed over to Laravel, which will generate the correct URL using the available parameters. The route name must be configured in the `config/shop.php` file, e.g.

```php
'client' => [
    'html' => [
        'mycomponent' => [
            'mypart' => [
                'url' => [
                    'target' => 'aimeos_shop_mypage',
                ],
            ],
        ],
    ],
]
```

The "mycomponent" and "mypart" names must be replaced by the name of your Aimeos HTML client component and the part you've implemented.

# Add locale selector

For shops offering multiple languages, currencies or both, Aimeos contains a locale selector component that renders menus of the configured language/currency combinations, so visitors are able to choose their preferred language and/or currency. By default, both will be part of the URL afterwards.

How to add locales for language/currency combinations is described in the [user manual](../manual/locales.md).

## Configuration

To make the locale selector available in the templates, you need to add the component name to the page configuration. Replace the relevant settings for the "page" configuration in your `config/shop.php` file which these lines:

```php
'page' => [
	'account-index' => [
		'locale/select','account/history','account/favorite','account/watch',
		'basket/mini','catalog/session'
	]
	'basket-index' => ['locale/select','basket/standard','basket/related'],
	'catalog-detail' => [
		'locale/select','basket/mini','catalog/stage',
		'catalog/detail','catalog/session'
	],
	'catalog-list' => [
		'locale/select','basket/mini','catalog/filter',
		'catalog/stage','catalog/lists'
	],
	// ...
]
```

They add the "locale/select" component to the account, basket, catalog detail and catalog list templates where they can be rendered afterwards.

If you upgrade from earlier versions, please make sure that your shop configuration (in `config/shop.php`) contains these lines too:

```php
'client' => [
	'html' => [
		'locale' => [
			'select' => [
				'currency' => [
					'param-name' => 'currency',
				],
				'language' => [
					'param-name' => 'locale',
				],
			],
		],
	],
],
```

## Templates

Laravel applications can overwrite the templates of packages by copying a modified version of the template to the `resources/views/vendor/aimeos/shop/` directory. This is done automatically during the installation via composer.

In each page template where the locale selector should be available, you need to add the lines for rendering the header and body section of the locale selector:

```php
@section('aimeos_header')
    ...
    <?= $aiheader['locale/select'] ?>
@stop

@section('aimeos_head')
    ...
    <?= $aibody['locale/select'] ?>
@stop
```

Templates that should be modified:

* account/index.blade.php
* basket/index.blade.php
* catalog/detail.blade.php
* catalog/list.blade.php

Depending on the section you've added the body of the locale selector to, it will be rendered at different places. For more details about templates, please have a look into the section about [adapting pages](#adapt-pages).

## Routes

Language and currency ID chosen by the visitor are part of the URL by default, so they are explicit and can be cached (contrary to information based on session data). To make this work, you need to add a route prefix in your `config/shop.php`:

```php
'routes' => [
    'account' => ['prefix' => '{locale}/{currency}', ... ],
    'default' => ['prefix' => '{locale}/{currency}', ... ],
    'confirm' => ['prefix' => '{locale}/{currency}', ... ],
    'update' => ['prefix' => '{locale}/{currency}', ... ],
]
```

These two lines require that the language ("locale") and currency ID must be part of all URLs besides the "admin" ones. If you only need the language, you should use this instead:

```php
'routes' => [
    'account' => ['prefix' => '{locale}', ... ],
    'default' => ['prefix' => '{locale}', ... ],
    'confirm' => ['prefix' => '{locale}', ... ],
    'update' => ['prefix' => '{locale}', ... ],
]
```

## Adapt selector

The locale selector is a normal component with subparts, that can be adapted like any other component. If you e.g. only need a language or currency menu, you can remove the subpart you don't need via the [client/html/locale/select/standard/subparts](../config/client-html/locale-select#subparts) configuration.

Adapting the layout of the locale selector is possible via CSS.

# Extend Aimeos

## Create an extension

Aimeos and the Aimeos Laravel package are very powerful but there are numerous features that are only available through additional extensions. Often, your project also requires special features that makes it different from other web sites built with Aimeos.

But changing or extending the Aimeos Laravel package itself is a bad idea because you will then lose the ability to update that extension. To solve this, the Aimeos Laravel package allows you to integrate additional Aimeos extensions. Simply place your additional extensions in the `./ext/` directory of your Laravel application.

!!! tip
    You can easily create a new Aimeos extension by using the [extension generator](https://aimeos.org/extensions).

## Use the Aimeos objects

If you need to instantiate the Aimeos controllers or managers directly from your Laravel application and call their methods, you have to supply a [context object](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Context/Item/Iface.php).

This object is a dependency injection container that offers access to configuration settings, database connections, session and content cache as well as translation facilities. You can get an instance in Laravel via the "app" service container or the "App" facade:

```php
// in a controller action
$context = $this->app->make('aimeos.context')->get();
// in a command task
$context = $this->getLaravel()->make('aimeos.context')->get(false);
// anywhere else
$context = App::make('aimeos.context')->get(false);
```

The parameter of the *get()* method determines if a locale object with site, language and currency based on the request parameters will be automatically added to the context together with the translation facilities. Certainly, this is only possible in MVC controller actions where the required parameters are available as part of the request.

Everywhere else, you need to retrieve this values from somewhere else, e.g. the configuration. Then, you can use the *bootstrap()* method of the [locale manager](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Locale/Manager/Iface.php) to retrieve the locale item yourself:

```php
$manager = \Aimeos\MShop::create( $context, 'locale' );
$item = $manager->bootstrap( '<sitecode>', '<languageid>', '<currencyid', true );
$context->setLocale( $item );
```

The language and currency IDs are optional and the first matching locale item from the *mshop_locale* table in the database will be used. If there are no entries in the *mshop_locale* table because you want to manage the data in a custom administration interface, you can create an empty locale object yourself:

```php
$manager = \Aimeos\MShop::create( $context, 'locale' );
$item = $manager->createItem()->setLanguageId( 'en' );
$context->setLocale( $item );
```

It's a good idea to set at least the currently used language ID because then you are able to add the translation facilities for this language too and there won't be any exception if some code wants to translate a string:


```php
// use the appropriate way depending on your environment
$context->setI18n( $this->app->make( 'aimeos.i18n' )->get( ['en'] ) );
```

Alternatively, if you don't want any translation, you can add a "Null" object instead. It returns the singular or plural string untranslated and for this decision it needs the language ID to determine the right singular/plural rule:

```php
$context->setI18n( ['en' => new \Aimeos\MW\Translation\None( 'en' )] );
```

Afterwards, you are able to create every object from the Aimeos core and save, retrieve or delete the stored data. You should never use the "new" operator to create a new objects because the implementation variant depends on the configuration and decorators are added automatically. Instead, use the *Aimeos\MShop* class or any more specific factory to create new objects, e.g.

```php
$manager = \Aimeos\MShop::create( $context, 'product' );
$filter = $manager->filter()->add( 'product.code', '==', 'test' );

foreach( $manager->searchItems( $search ) as $id => $item ) {
    // print_r( $item );
}
```
