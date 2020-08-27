# Adapt pages

When talking about pages we think of the full HTML response that is sent to the browser of the visitors after they entered a [shop URL](http://symfony.demo.aimeos.org/default/en/EUR/list). It includes the output from the Aimeos components embedded into the [base template](https://github.com/aimeos/aimeos-symfony#setup) you've provided after installation. This article focuses on changing the components that are visible on a page. If you want to adapt only the theme, please read the article about [theming of the shop components](../../frontend/html/theme-basics.md).

All Aimeos pages can contain a list of pre-defined blocks:

* **aimeos_styles** ( additional CSS files)
* **aimeos_scripts** (additional JS files)
* **aimeos_header** (HTML head tags like product title and meta information)
* **aimeos_head** (head section including the small basket for example)
* **aimeos_nav** (shop navigation and faceted search)
* **aimeos_stage** (stage area including breadcrumb navigation)
* **aimeos_body** (main content for product lists, details or the checkout process)
* **aimeos_aside** (user related content, e.g. last seen products)

If there is some content inside these blocks will be decided by the templates for the actions of the controllers. You can find these templates in the [./Resources/views/](https://github.com/aimeos/aimeos-symfony/tree/master/Resources/views) directory and its subdirectories of the Aimeos shop bundle.

## Don't change the bundle

Even if it seems the easiest way to modify the templates and configuration files in the Aimeos shop bundle directly, it's really a bad idea! You will loose the ability to update the Aimeos bundle without resetting everything to the standard configuration and templates. Instead, Symfony provides an easy way to overwrite the configuration as well as the templates of any bundle.

To **overwrite the configuration**, you only have to add the modified configuration settings to your `./config/packages/aimeos_shop.yaml` file, e.g.

```yaml
aimeos_shop:
    page:
        "account-index": ['account/history']
```

would overwrite the list of components for the "MyAccount" page from the Aimeos bundle. In the same way you can **replace existing templates** by copying the original template to the `./templates/bundles/AimeosShopBundle/Page/` directory of your Symfony application and modify it according to your needs.

## Reorder components

The easiest possibility is changing the order of the single components inside the pre-defined blocks. Let's use the page template for the account page as example:

```twig
{% extends 'AimeosShopBundle::base.html.twig' %}

{% block aimeos_header %}
    {{ aiheader['basket/mini']|raw }}
    {{ aiheader['account/history']|raw }}
    {{ aiheader['account/favorite']|raw }}
    {{ aiheader['account/watch']|raw }}
    {{ aiheader['catalog/session']|raw }}
{% endblock %}

{% block aimeos_head %}
    {{ aibody['basket/mini']|raw }}
{% endblock %}

{% block aimeos_body %}
    {{ aibody['account/history']|raw }}
    {{ aibody['account/favorite']|raw }}
    {{ aibody['account/watch']|raw }}
{% endblock %}

{% block aimeos_aside %}
    {{ aibody['catalog/session']|raw }}
{% endblock %}
```

The `{% extends ... %}` instruction defines the template this one will inherit the rest of the layout from. To change the order of the components in the "{% block aimeos_body %}, you can simple reorder the single lines inside the `{% block ... %} ... {% endblock %}` tags, e.g:

```twig
{% block aimeos_body %}
    {{ aibody['account/favorite']|raw }}
    {{ aibody['account/watch']|raw }}
    {{ aibody['account/history']|raw }}
{% endblock %}
```

This would move the order history component to the end of the body container in the HTML response.

## Add components

Adding more components to an existing page consists of two steps:

* Add the component name to the overwritten page configuration
* Insert the body and header output in the copied page template

By default, not all shop components are available on every page as this would create a lot of unnecessary load on your server. Instead, only the components are rendered and handed over to the template which are configured in the "page" section of the `./Resource/config/aimeos_shop.yml` file, e.g.

```yaml
aimeos_shop:
    page:
        "account-index": ['account/history','account/favorite','account/watch','basket/mini','catalog/session']
```

Available components are listed for each Page controller action and they are identified using the [directory structure](https://github.com/aimeos/ai-client-html/tree/master/client/html/src/Client/Html) of the HTML clients in the core. Thus, the account history component in the "Client/Html/Account/History" directory is addressed via the string "account/history".

Similarly, the product listing component is identified by "catalog/list" or the product detail component by "catalog/detail". This works for all components besides the ones that are in the "Client/Html/Common" and "Client/Html/Email" directory.

!!! warning
    Please keep in mind that some components need specific parameters like the "catalog/detail" component, which requires at least a value for the "d_prodid" parameter. There's a [complete list of parameters used](../../frontend/html/parameter-names.md) available for reference.

For example, if you want to add the catalog filter component to your "MyAccount" page as well, you can add its name inside the square brackets of the page component list:

```yaml
aimeos_shop:
    page:
        "account-index": ['account/history','account/favorite','account/watch','basket/mini','catalog/session','catalog/filter']
```

Here, the order of the component names doesn't matter but the header and body of the catalog filter component will be now available inside the "aibody" and "aiheader" array variables in the template of the account page controller action. Nevertheless, there's no output yet because you need to tell the template where their content should be rendered to:

```twig
{% block aimeos_header %}
    ...
    {{ aiheader['catalog/filter']|raw }}
{% endblock %}

{% block aimeos_nav %}
    {{ aibody['catalog/filter']|raw }}
{% endblock %}
```

For the body, we use the "aimeos_nav" block so the filter menu will be located in the same place like in the other pages but you are free to put it in every block you want except the "aimeos_header" block. Contrary to that, the header data must always be placed in the "aimeos_header" block to be effective but the order inside the "aimeos_header" block is most of the time not important.

Both lines need the **"|raw"** modifier after specifying which component to display. This avoids the HTML being escaped by the Twig template engine.

## Remove components

Removing components is simple as you only have to provide a page template without the aibody and aiheader lines of the component, e.g.:

```twig
{% extends 'AimeosShopBundle::base.html.twig' %}

{% block aimeos_header %}
    {{ aiheader['basket/mini']|raw }}
    {{ aiheader['account/history']|raw }}
    {{ aiheader['account/favorite']|raw }}
    {{ aiheader['account/watch']|raw }}
{% endblock %}

{% block aimeos_head %}
    {{ aibody['basket/mini']|raw }}
{% endblock %}

{% block aimeos_body %}
    {{ aibody['account/history']|raw }}
    {{ aibody['account/favorite']|raw }}
    {{ aibody['account/watch']|raw }}
{% endblock %}
```

That template wouldn't output the "catalog/session" body and header HTML but to avoid rending them at all, you need to overwrite the page configuration as well:

```yaml
aimeos_shop:
    page:
        "account-index": ['account/history','account/favorite','account/watch','basket/mini']
```

!!! tip
    For testing, it's OK to remove only the lines from the page templates but you get significant speedups in your production environment by providing a modified page configuration too.

# Create pages

The Aimeos bundle contains all pages which are necessary to create a complete online shop. But sometimes you might want some additional pages that should contain Aimeos components too, like the small basket or the last seen products from the catalog session component. If you only want to modify the output of existing pages, please take a look into the section about [adapting pages](#adapt-pages) instead.

Assuming that you already created a controller, action and a template for your new page (if not, take a look into the [Symfony documentation](https://symfony.com/doc/current/page_creation.html)), this article contains the required steps to add the Aimeos components as well.

## Adapt your controller

The easiest and most efficient way to retrieve the body and header parts from Aimeos components is to use the "aimeos_page" service and call the `getSections()` method inside your controller action:

```php
namespace Acme\DemoBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class ExampleController extends Controller
{
    public function indexAction()
    {
        $params = [];
        $shop = $this->container->get( 'shop' );

        foreach( $this->container->getParameter( 'aimeos_shop.page' )['catalog-count'] as $name )
        {
            $params['aiheader'][$name] = $shop->get( $name )->getHeader();
            $params['aibody'][$name] = $shop->get( $name )->getBody();
        }

        return $this->render( 'AcmeDemoBundle:Example:index.html.twig', $params );
    }
}
```

The result of the first line will be an array with keys for "aibody" and "aiheader" which contains associative arrays of the component name and the rendered HTML itself, e.g.

```php
$ouput = [
    'aibody' => [
        'basket/mini' => '<div> ... rendered HTML ... ',
        'catalog/session' => '<div> ... rendered HTML ... '
	],
    'aiheader' => [
        'basket/mini' => '... HTML head tags ...',
        'catalog/session' => '... HTML head tags ...'
	]
];
```

This array is then passed to the `render()` method so there will be "aibody" and "aiheader" variables available in the template.

## Configure the components

Up to now, there would be no output because you haven't defined that you need some components in your template. This is done in the `./config/packages/aimeos_shop.yaml` file of your Symfony application. Remind yourself of the parameter passed to the getSections() method call: We've used "mypage" in this example and this will be the required configuration key:

```yaml
aimeos_shop:
    page:
        mypage: ['basket/mini','catalog/session']
```

Now you have told your action that the "mypage" parameter should render the body and header output for the "basket/mini" and the "catalog/session" components.

Available components are identified using the [directory structure](https://github.com/aimeos/ai-client-html/tree/master/client/html/src/Client/Html) of the HTML clients in the core. Thus, the catalog session component in the "Client/Html/Catalog/Session" directory is addressed via the string "catalog/session".

Similarly, the product listing component is identified by "catalog/list" or the product detail compoent by "catalog/detail". This works for all compoents besides the ones that are in the "Client/Html/Common" and "Client/Html/Email" directory.

!!! warning
    Please keep in mind that some components need specific parameters like the "catalog/detail" component, which requires at least a value for the "d_prodid" parameter. There's a [complete list of parameters used](../../frontend/html/parameter-names.md) available for reference.

## Modify your template

After adding the configuration, there are two variables in your template available containing arrays: "aibody" and "aiheader". They store the rendered HTML that should now be displayed somewhere in your template which should contain these blocks:

```twig
{% extends 'AimeosShopBundle::base.html.twig' %}

{% block aimeos_header %}
{% endblock %}

{% block aimeos_head %}
{% endblock %}

{% block aimeos_nav %}
{% endblock %}

{% block aimeos_stage %}
{% endblock %}

{% block aimeos_body %}
{% endblock %}

{% block aimeos_aside %}
{% endblock %}
```

You must extend your template from the base template of the Aimeos shop bundle. Otherwise, the CSS and Javascript files would be missing and no styling would be applied resp. no client side code is available for the full functionality.

The single blocks correspond to the blocks of your [root layout template](https://github.com/aimeos/aimeos-symfony#setup) which you have created after installation. Depending on where you want to display the output, you have to insert the necessary line into the corresponding block, for example

```twig
{% block aimeos_header %}
    {{ aiheader['basket/mini']|raw }}
    {{ aiheader['catalog/session']|raw }}
{% endblock %}

{% block aimeos_head %}
    {{ aibody['basket/mini']|raw }}
{% endblock %}

{% block aimeos_aside %}
    {{ aibody['catalog/session']|raw }}
{% endblock %}
```

For the basket mini body, we use the "aimeos_head" block so the small basket will be located in the same place like in the other pages but you are free to put it in every block you want except the "aimeos_header" block. The same applies to the catalog session body in the "aimeos_aside" block.

The header data must be always placed in the "aimeos_header" block to be effective but the order inside the "aimeos_header" block is most of the time not important. Both lines need the `|raw` modifier after specifying which component to display. This avoids the HTML being escaped by the Twig template engine.

If there are empty blocks after you've added all the output, you can remove them safely.

# Custom routes

Routes are defined in the [routing.yml](https://github.com/aimeos/aimeos-symfony/blob/master/Resources/config/routing.yml) of the Aimeos shop bundle and a set of standard routes is provided by default. Each route has at least a name, the corresponding path and some default parameter. At least the controller name is mandatory:

```yaml
<route name>:
     path: <path of the route>
     defaults: { _controller: AimeosShopBundle:<controller name>:<action name> }
```

Each route creates links to one page of your application. The route names are important for the core library because the Symfony router needs their names for generating the correct routes for the given parameter.

## Route names

The names of the standard routes are predefined in the [routing.yml](https://github.com/aimeos/aimeos-symfony/blob/master/Resources/config/routing.yml) file. Besides the "admin" routes which are not listed here, their names are:

* **aimeos_shop_account** ("my account" page for each user)
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

## Adapt existing routes

For all existing routes, you can change its path and the default parameters by redefining the routes in the global `./config/routing.yaml` file using the same name. For example, to change the path of the "aimeos_shop_terms" to "/terms_and_conditions", you only need to use that path in the global `./config/routing.yaml` file:

```yaml
aimeos_shop_terms:
    path: /terms_and_conditions
    defaults: { _controller: AimeosShopBundle:Page:terms }
```

Similarly, changing the controller and action name to a custom one ("Terms" and "index") implemented in your application is done by adapting the `_controller` value in the "defaults" section of the route:

```yaml
aimeos_shop_terms:
    path: /terms
    defaults: { _controller: MyBundleName:Terms:index }
```

More details can be found in the [Symfony routing documentation](https://symfony.com/doc/current/book/routing.html).

## Routes for multiple site, languages and currencies

Aimeos is able to manage many sites in one installation with different languages and currencies for each site. If you have such a setup with at least two sites, languages or currencies, you need to adapt your `./config/routing.yaml` file which contains these lines after installing the Aimeos Symfony bundle via composer:

```yaml
aimeos_shop:
    resource: "@AimeosShopBundle/Resources/config/routing.yml"
    prefix:   /
```

The line containing the "prefix" keyword can be used not only to add a fixed prefix string like "/shop" but also be changed to support these placeholders for the route definition:

* **{site}** (unique site code from "code" field in the "mshop_locale_site" table)
* **{locale}** (language ID from the "langid" field in the "mshop_locale" table)
* **{currency}** (currency ID from the "currencyid" field in the "mshop_locale" table)

An example with site, language and currency would be:

```yaml
aimeos_shop:
    resource: "@AimeosShopBundle/Resources/config/routing.yml"
    prefix:   /{site}/{locale}/{currency}
    defaults: { site: 'default', locale: 'en', currency: 'EUR' }
```

The parameters and values in the "defaults" line should be set if no values for the parameters are given via the URL. This prevents invalid links and creates links using the default values.

You can also reorder the placeholders the way you prefer like moving the `{locale}` placeholder to the front. If your shop doesn't use more than one site, language or currency, you can also leave out those placeholders. The Aimeos shop will automatically use the default values in this case.

For the "site" parameter it's always "default" and for the language and currency the ones you've defined in the "Locale" tab of the administration interface. By changing the "prefix" to anything else than "/", you must also redefine the route definitions for the administration interface and add them to your `./config/routing.yaml file too:

```yaml
aimeos_shop_admin_json:
    path: /admin/do
    defaults: { _controller: AimeosShopBundle:Admin:do }

aimeos_shop_admin:
    path: /admin/{site}/{lang}/{tab}
    defaults: { _controller: AimeosShopBundle:Admin:index, site: default, lang: en, tab: 0 }
```

If you forget to do this, you will get an **error when calling the administration interface** as the placeholders can only be used once per route definition. Using e.g. the "{site}" placeholder in the "prefix" would then lead to a route definition like `/{site}/admin/{site}/{lang}/{tab}` which is invalid.

!!! warning
    If you modify the "prefix" setting, you also have to adapt the [authentication method patterns](customize.md#authentication-methods) and the [access control paths](customize.md#access-control) for the "Profile" page.

## Add new routes

If you've implemented a new Aimeos core component which generates URLs to a new page, you have to add a new custom route. The route name can be freely chosen but for clarity, you should prefix it with "aimeos_shop_", e.g.

```yaml
aimeos_shop_mypage:
     path: /new_page
     defaults: { _controller: MyBundleName:Mycontroller:myaction }
```

The Aimeos core component now needs to know the name of the new route. It's then handed over to the Symfony router which will generate the correct URL using the available parameters. The route name must be configured in the `./config/packages/aimeos_shop.yaml` file, e.g.

```yaml
aimeos_shop:
    client:
        html:
            mycomponent:
                mypart:
                    url:
                        target: aimeos_shop_mypage
```

The "mycomponent" and "mypart" names must be replaced by the name of your Aimeos HTML client component and the part you've implemented.

# Add locale selector

For shops offering multiple languages, currencies or both, Aimeos contains a locale selector component that renders menus of the configured language/currency combinations, so visitors are able to choose their preferred language and/or currency. By default, both will be part of the URL afterwards.

How to add locales for language/currency combinations is described in the [user manual](../../manual/locales.md).

## Configuration

To make the locale selector available in the templates, you need to add the component name to the page configuration. Add these settings for the "page" configuration in your `./config/packages/aimeos_shop.yaml` file:

```yaml
aimeos_shop:
    page:
        account-index: ['locale/select','account/history','account/favorite','account/watch','basket/mini','catalog/session']
        basket-index: ['locale/select','basket/standard','basket/related']
        catalog-detail: ['locale/select','basket/mini','catalog/stage','catalog/detail','catalog/session']
        catalog-list: ['locale/select','basket/mini','catalog/filter','catalog/stage','catalog/lists']
```

They add the "locale/select" component to the account, basket, catalog detail and catalog list templates where they can be rendered afterwards.

## Templates

Symfony applications can overwrite the templates of bundles by copying a modified version of the template to the `./app/Resources/AimeosShopBundle/views/` directory.

In each page template where the locale selector should be available, you need to add the lines for rendering the header and body section of the locale selector:

```twig
{% block aimeos_header %}
    ...
    {{ aiheader['locale/select']|raw }}
{% endblock %}

{% block aimeos_head %}
    ...
    {{ aibody['locale/select']|raw }}
{% endblock %}
```

Templates that should be modified:

* Account/index.html.twig
* Basket/index.html.twig
* Catalog/detail.html.twig
* Catalog/list.html.twig

Depending on the section you've added the body of the locale selector to, it will be rendered at different places. For more details about templates, please have a look into the section about [adapting pages](#adapt-pages).

## Routes

Language and currency ID chosen by the visitor are part of the URL by default, so they are explicit and can be cached (contrary to information based on session data). To make this work, you need to redefine all routes besides the "adm" (admin) routes with a prefix in your `./config/routing.yaml`:

```yaml
aimeos_shop_account:
    path: /{locale}/myaccount
    defaults: { _controller: AimeosShopBundle:Account:index, locale: 'en' }

# ...
```

## Adapt selector

The locale selector is a normal component with subparts, that can be adapted like any other component. If you e.g. only need a language or currency menu, you can remove the subpart you don't need via the [client/html/locale/select/standard/subparts](../../config/client-html/locale-select.md#subparts) configuration.

Adapting the layout of the locale selector is possible via CSS.

# Extend Aimeos

## Create an extension

Aimeos and the Aimeos Symfony bundle are very powerful but there are numerous features that are only available through additional extensions. Often, your project also requires special features that makes it different from other web sites build with Aimeos. But extending the Aimeos Symfony bundle itself is a bad thing because you will loose the ability to update the extension.

To solve this, the Aimeos Symfony bundle allows you to integrate additional Aimeos extensions. Simply place your additional extensions in the `./ext/ directory of your Symfony application.

!!! tip
    You can easily create a new Aimeos extension by using the [extension generator](https://aimeos.org/extensions/)

## Use the Aimeos objects

If you need to instantiate the Aimeos controllers or managers directly from your Symfony application and call their methods, you have to supply a [context object](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Context/Item/Iface.php). This object is a dependency injection container that offers access to configuration settings, database connections, session and content cache as well as translation facilities. You can get an instance in Symfony via the service container:

```php
// in a controller action
$context = $this->get( 'aimeos_context' )->get();
// in a command task
$context = $this->getContainer()->get( 'aimeos_context' )->get(false);
```

For a list of all possibilities, please have a look into the [Symfony documentation](https://symfony.com/doc/current/components/dependency_injection/types.html).

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
$context->setI18n( $this->get( 'aimeos_i18n' )->get( ['en'] ) );
```

Alternatively, if you don't want any translation, you can add a "Null" object instead. It returns the singular or plural string untranslated and for this decision it needs the language ID to determine the right singular/plural rule:

```php
$context->setI18n( ['en' => new \Aimeos\MW\Translation\None( 'en' )] );
```

Afterwards, you are able to create every object from the Aimeos core and save, retrieve or delete the stored data. You should never use the "new" operator to create a new objects because the implementation variant depends on the configuration and decorators are added automatically. Instead, use the *Aimeos\MShop* class or any more specific factory to create new objects, e.g.

```php
$manager = \Aimeos\MShop::create( $context, 'product' );
$filter = $manager->filter()->add( 'product.code', '==', 'test' );

foreach( $manager->searchItems( $filter ) as $id => $item ) {
    // print_r( $item );
}
```
