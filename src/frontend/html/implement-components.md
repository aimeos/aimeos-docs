In rare cases you might want to create a new shop component when none of the existing ones really fits into what you need. It's rather easy to create one but the **adapters for the frameworks and the applications** need to integrate your new component to utilize it.

It's generally a good idea to discuss a new component in the [Aimeos forum](https://aimeos.org/help) first and contribute your code to the official core. Otherwise, you would have to do everything yourself.

This article highlights the differences of a component compared to a subpart for an existing component. Please read the article about [implementing a new subpart](create-subparts.md) first for a decent understanding of the basics.

# Class structure

Because a component must implement the same interface as all subparts and thus, also extends from the same parent class, the methods are the same:

```php
namespace Aimeos\Client\Html\Catalog\Detail;

class Standard
    extends \Aimeos\Client\Html\Common\Client\Factory\Base
    implements Aimeos\Client\Html\Common\Client\Factory\Iface
{
    private $tags = [];
    private $expire;
    private $view;


    public function body( $uid = '' ) : string
    {
        // optional
    }

    public function header( $uid = '' ) : ?string
    {
        // optional
    }

    public function init()
    {
        // optional
    }

    public function getSubClient( string $type, string $name = null ) : \Aimeos\Client\Html\Iface
    {
        // optional
    }

    protected function getSubClientNames() : array
    {
        // optional
    }
}
```

Differences arise from the required code inside these methods as they have to care about caching (if you want to) and exception handling. A component can implement the same optional methods as any subpart. For a detailed description of these methods, please refer to the article about [creating new subparts](create-subparts.md#optional-methods).

The [getSubClient()](create-subparts.md#getSubClient) and [getSubClientNames()](create-subparts.md#getSubClientNames) methods are also exactly the same as in any other subpart and won't be described in this article again.

# init()

This method is not affected by caching at all because its purpose is to execute code once during each request. The difference to `init()` methods of subclients is only that you need to catch thrown exceptions and assign error messages to the view if necessary.

If you don't need to process any input in your new component, you can copy & paste the code below into your new class:

```php
public function init()
{
    $context = $this->context();
    $view = $this->view();

    // your required code
    parent::init();
}
```

The only thing you have to **adapt is the name of the error list** assigned to the view. It should be named after your class name to something like `$view->...ErrorList`.

The cascade of `catch()` statements ensures that all exceptions are caught. Furthermore, all error messages translated that are passed to the view and shown to the customers. Unspecific exceptions are logged and only a generic error message is shown in the front-end to avoid giving away sensitive information.

You need to print these error messages in your component view which is described in the next section.

# Display error messages

The messages of the exceptions thrown in the different methods are assigned to the view using the `error` variable, which is an array of error messages. You need to add a snippet similar to this one at the top of your component body view:

```php
<?php if( isset( $this->errors ) ) : ?>
    <ul class="error-list">
<?php foreach( (array) $this->get( 'errors', [] ) as $errmsg ) : ?>
        <li class="error-item"><?= $this->encoder()->html( $errmsg ) ?></li>
<?php endforeach ?>
    </ul>
<?php endif ?>
```
These few lines of code create an HTML block that will contain all error messages. It will be styled by the used theme, so you don't have to care about this.

# With content caching

Components that can cache its output are extremely fast. Once the content is generated and stored, it can be retrieved within milliseconds and directly pushed to the browser. The downside is that some additional code is needed.

## body()

When caching comes into play, the first thing you have to think about is: What does your output depend on? Usually, two external sources can influence what content needs to be generated: The request parameters and the configuration settings. Both has to be part of the cache key.

In an Aimeos component, it's not difficult to encode both sources into the cache key. All parameters are prefixed depending on their source, e.g. parameters that are used for the catalog filter start with an "f", all catalog list parameters with a "l" and the parameters for the catalog detail page with a "d".

You only need to specify the prefixes of the parameters your component listens to. The configuration settings are build hierarchically, so the prefix that is shared by all subclients of your component is required. The rest is simply calling the `getCached()` and `setCached()` method from the parent class.

```php
public function body( string $uid = '' ) : string
{
    $view = $this->view();
    $config = $this->context()->config();

    $params = ['d_prodid', 'd_name'];
    $confkey = 'client/html/catalog/detail';

    if( $html = $this->cached( 'body', $uid, $params, $confkey ) ) {
        return $this->modify( $html, $uid );
    }

    $template = $config->get( 'client/html/catalog/detail/template-body', 'catalog/detail/body' );

    $view = $this->view = $this->view ?? $this->object()->data( $view, $this->tags, $this->expire );
    $html = $this->modify( $view->render( $template ), $uid );

    return $this->cache( 'body', $uid, $prefixes, $confkey, $html, $this->tags, $this->expire );
}
```

There's one thing to note when caching content: Sometimes, a subpart can't be cached because it depends on the sessions or cookies of the customers. In this case the whole content wouldn't be cachable at all. Fortunately, there's a solution for this problem: The `modify()` method allows any subclient to replace a section in the cached content.

The details for this are described in the article about [creating new subparts](create-subparts#modify). The important thing here is to call the `modify()` method provided by the parent class after successfully retrieving the cached content.

In doubt, have a look into a full example of a working [body() component method](https://github.com/aimeos/ai-client-html/blob/master/src/Client/Html/Catalog/Detail/Standard.php) which implements caching.

## header()

For `header()`, implementing caching is very similar to the implementation of `body()`. You also have to specify which parameters are used in your component and what's the shared configuration prefix for all settings. The calls to `getCached()` and `setCached()` require "header" to be passed to ensure that the content is stored for the header.

```php
public function header( string $uid = '' ) : string
{
    $view = $this->view();
    $config = $this->context()->config();

    if( $html = $this->cached( 'header', $uid, $prefixes, $confkey ) ) {
        return $this->modify( $html, $uid );
    }

    $template = $config->get( 'client/html/catalog/detail/template-header', 'catalog/detail/header' );

    $view = $this->view = $this->view ?? $this->object()->data( $this->view(), $this->tags, $this->expire );
    $html = $view->render( $template );

    return $this->cache( 'header', $uid, $prefixes, $confkey, $html, $this->tags, $this->expire );
}
```

Only keep in mind that you also need to call the `modify()` method after successfully retrieving the cached content. This allows subclients of your component the chance to replace their sections with their new content.

In doubt, have a look into a full example of a working [header() component method](https://github.com/aimeos/ai-client-html/blob/master/src/Client/Html/Catalog/Detail/Standard.php) which implements caching.

# Factory class

All components are instantiated by factories which care about creating the HTML client and decorating it with additional classes added via configuration. The factory class is a rather simple piece of code that contains only a `create()` method:

```php
namespace Aimeos\Client\Html\Catalog\Detail;

class Factory
    extends \Aimeos\Client\Html\Common\Factory\Base
    implements \Aimeos\Client\Html\Common\Factory\Iface
{
    public static function create( \Aimeos\MShop\Context\Item\Iface $context, array $paths, string $name = null ) : \Aimeos\Client\Html\Iface
    {
        if( $name null ) {
            $name = $context->config()->get( 'client/html/catalog/detail/name', 'Standard' );
        }

        $iface = '\\Aimeos\\Client\\Html\\Iface';
        $classname = '\\Aimeos\\Client\\Html\\Catalog\\Detail\\' . $name;

        if( ctype_alnum( $name ) === false ) {
            throw new \Aimeos\Client\Html\Exception( sprintf( 'Invalid characters in class name "%1$s"', $classname ) );
        }

        $client = self::createClient( $context, $classname, $iface );
        $client = self::addClientDecorators( $context, $client, 'catalog/detail' );

        return $client->setObject( $client );
    }
}
```

The code above is a factory for the catalog detail client. You can copy the code and replace the "Catalog\Detail" and "catalog/detail" strings with the name of your own component. For example, if you want to create a new "catalog homepage" component, you should replace the strings like this:

```
Catalog\Detail -> Catalog\Homepage
catalog/detail -> catalog/homepage
```

Component factories for other purposes can created the same way, e.g. for a "basket upsell" component, replace the strings in that way:

```
Catalog\Detail -> Basket\Upsell
catalog/detail -> basket/upsell
```

The factory and the default implementation of your component must be saved to the appropriate directory, i.e. to the *./src/Catalog/Homepage* or *./src/Basket/Upsell* directory of your own extension.
