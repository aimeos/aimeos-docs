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
    private $subPartPath = 'client/html/catalog/detail/subparts';
    private $subPartNames = [];
    private $tags = [];
    private $expire;
    private $view;


    public function body( $uid = '' ) : string
    {
    }

    public function header( $uid = '' ) : ?string
    {
    }

    public function getSubClient( string $type, string $name = null ) : \Aimeos\Client\Html\Iface
    {
    }

    public function init()
    {
    }

    protected function getSubClientNames() : array
    {
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

    try
    {
        // your required code
        parent::init();
    }
    catch( \Aimeos\Client\Html\Exception $e )
    {
        $error = [$context->translate( 'client', $e->getMessage() )];
        $view->detailErrorList = array_merge( $view->get( 'detailErrorList', [] ), $error );
    }
    catch( \Aimeos\Controller\Frontend\Exception $e )
    {
        $error = [$context->translate( 'controller/frontend', $e->getMessage() )];
        $view->detailErrorList = array_merge( $view->get( 'detailErrorList', [] ), $error );
    }
    catch( \Aimeos\MShop\Exception $e )
    {
        $error = [$context->translate( 'mshop', $e->getMessage() )];
        $view->detailErrorList = array_merge( $view->get( 'detailErrorList', [] ), $error );
    }
    catch( \Exception $e )
    {
        $error = [$context->translate( 'client', 'A non-recoverable error occured' )];
        $view->detailErrorList = array_merge( $view->get( 'detailErrorList', [] ), $error );
        $this->logException( $e );
    }
}
```

The only thing you have to **adapt is the name of the error list** assigned to the view. It should be named after your class name to something like `$view->...ErrorList`.

The cascade of `catch()` statements ensures that all exceptions are caught. Furthermore, all error messages translated that are passed to the view and shown to the customers. Unspecific exceptions are logged and only a generic error message is shown in the front-end to avoid giving away sensitive information.

You need to print these error messages in your component view which is described in the next section.

# Display error messages

The exceptions caught in the methods and assigned to the view should be shown to the customers so they know what's going on. For this, you need to add a snippet similar to this one at the top of your component body view:

```php
<?php if( isset( $this->detailErrorList ) ) : ?>
    <ul class="error-list">
<?php foreach( (array) $this->detailErrorList as $errmsg ) : ?>
        <li class="error-item"><?= $this->encoder()->html( $errmsg ) ?></li>
<?php endforeach ?>
    </ul>
<?php endif ?>
```

Remember to **adapt the parameter name** of `detailErrorList` to the name you've used in the methods of your new component class. These few lines of code create an HTML block that will contain all error messages. It will be styled by the used theme, so you don't have to care about this.

# No caching

If the output of your new component isn't suitable for caching, things are a bit easier for the `body()` and `header()` method because you only need to catch the exceptions as for the `init()` method.

## body()

Very similar to the `init()` method, you have to catch all exceptions, translate them if possible and assign them to the view so the visitors are notified about the errors. The example method below only contains the parts that are different to those of the [method from the subpart clients](create-subparts.md#body):

```php
public function body( string $uid = '' ) : string
{
    $context = $this->context();
    $view = $this->view();

    try
    {
        if( !isset( $this->view ) ) {
            $view = $this->view = $this->object()->data( $view, $this->tags, $this->expire );
        }

        $html = '';
        foreach( $this->getSubClients() as $subclient ) {
            $html .= $subclient->setView( $view )->body( $uid );
        }
        $view->detailBody = $html;
    }
    catch( \Aimeos\Client\Html\Exception $e )
    {
        $error = [$context->translate( 'client', $e->getMessage() )];
        $view->detailErrorList = array_merge( $view->get( 'detailErrorList', [] ), $error );
    }
    catch( \Aimeos\Controller\Frontend\Exception $e )
    {
        $error = [$context->translate( 'controller/frontend', $e->getMessage() )];
        $view->detailErrorList = array_merge( $view->get( 'detailErrorList', [] ), $error );
    }
    catch( \Aimeos\MShop\Exception $e )
    {
        $error = [$context->translate( 'mshop', $e->getMessage() )];
        $view->detailErrorList = array_merge( $view->get( 'detailErrorList', [] ), $error );
    }
    catch( \Exception $e )
    {
        $error = [$context->translate( 'client', 'A non-recoverable error occured' )];
        $view->detailErrorList = array_merge( $view->get( 'detailErrorList', [] ), $error );
        $this->logException( $e );
    }

    $tplconf = 'client/html/catalog/detail/template-body';
    $default = 'catalog/detail/body';

    return $view->render( $view->config( $tplconf, $default ) );
}
```

Don't forget to **adapt the `detailErrorList` view variable** to your component name. It must be the same as used in your error displaying code of your view.

In doubt, have a look into a full example of a working [body() component method without caching](https://github.com/aimeos/ai-client-html/blob/master/client/html/src/Client/Html/Catalog/Session/Standard.php).

## header()

Compared to the `body()` method, `header()` is really simple because there's no way to display any errors that have been occured. Instead, you have to log them all and return no output. The code example below only contains the lines that are different from the [header() method of a subpart client](create-subparts.md#header):

```php
public function body( string $uid = '' ) : string
{
    $view = $this->view();

    try
    {
        if( !isset( $this->view ) ) {
            $view = $this->view = $this->object()->data( $view, $this->tags, $this->expire );
        }

        $html = '';
        foreach( $this->getSubClients() as $subclient ) {
            $html .= $subclient->setView( $view )->header( $uid );
        }
        $view->detailHeader = $html;
    }
    catch( Exception $e )
    {
        $this->context()->getLogger()->log( $e->getMessage() . PHP_EOL . $e->getTraceAsString() );
        return;
    }

    $tplconf = 'client/html/catalog/detail/template-header';
    $default = 'catalog/detail/header-stanard';

    $html = $view->render( $view->config( $tplconf, $default ) );

    return $html;
}
```

In doubt, have a look into a full example of a working [header() component method without caching](https://github.com/aimeos/ai-client-html/blob/master/client/html/src/Client/Html/Catalog/Session/Standard.php).

# With content caching

Components that can cache its output are extremely fast. Once the content is generated and stored, it can be retrieved within milliseconds and directly pushed to the browser. The downside is that some additional code is needed.

## body()

When caching comes into play, the first thing you have to think about is: What does your output depend on? Usually, two external sources can influence what content needs to be generated: The request parameters and the configuration settings. Both has to be part of the cache key.

In an Aimeos component, it's not difficult to encode both sources into the cache key. All parameters are prefixed depending on their source, e.g. parameters that are used for the catalog filter start with an "f", all catalog list parameters with a "l" and the parameters for the catalog detail page with a "d".

You only need to specify the prefixes of the parameters your component listens to. The configuration settings are build hierarchically, so the prefix that is shared by all subclients of your component is required. The rest is simply calling the `getCached()` and `setCached()` method from the parent class.

```php
public function body( string $uid = '' ) : string
{
    $prefixes = ['d'];
    $confkey = 'client/html/catalog/detail';

    if( ( $html = $this->getCached( 'body', $uid, $prefixes, $confkey ) ) === null ) )
    {
        // code is the same as for the uncached variant

        $html = $view->render( $view->config( $tplconf, $default ) );

        $this->setCached( 'body', $uid, $prefixes, $confkey, $html, $this->tags, $this->expire );
    }
    else
    {
        $html = $this->modifyBody( $html, $uid );
    }

    return $html;
}
```

There's one thing to note when caching content: Sometimes, a subpart can't be cached because it depends on the sessions or cookies of the customers. In this case the whole content wouldn't be cachable at all. Fortunately, there's a solution for this problem: The `modifyBody()` method allows any subclient to replace a section in the cached content.

The details for this are described in the article about [creating new subparts](create-subparts#modifyBody). The important thing here is to call the `modifyBody()` method provided by the parent class after successfully retrieving the cached content.

In doubt, have a look into a full example of a working [body() component method](https://github.com/aimeos/ai-client-html/blob/master/client/html/src/Client/Html/Catalog/Detail/Standard.php) which implements caching.

## header()

For `header()`, implementing caching is very similar to the implementation of `body()`. You also have to specify which parameters are used in your component and what's the shared configuration prefix for all settings. The calls to `getCached()` and `setCached()` require "header" to be passed to ensure that the content is stored for the header.

```php
public function header( string $uid = '' ) : string
{
    $prefixes = ['d'];
    $confkey = 'client/html/catalog/detail';

    if( ( $html = $this->getCached( 'header', $uid, $prefixes, $confkey ) ) null )
    {
        // same code as for the uncached variant

        $html = $view->render( $view->config( $tplconf, $default ) );

        $this->setCached( 'header', $uid, $prefixes, $confkey, $html, $this->tags, $this->expire );
    }
    else
    {
        $html = $this->modifyHeader( $html, $uid );
    }

    return $html;
}
```

In `header()`, the exception handling is much simpler as you only need to log any exception. Only keep in mind that you also need to call the `modifyHeader()` method after successfully retrieving the cached content. This allows subclients of your component the chance to replace their sections with their new content.

In doubt, have a look into a full example of a working [header() component method](https://github.com/aimeos/ai-client-html/blob/master/client/html/src/Client/Html/Catalog/Detail/Standard.php) which implements caching.

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

The factory and the default implementation of your component must be saved to the appropriate directory, i.e. to the *./client/html/src/client/html/catalog/homepage* or *./client/html/src/client/html/basket/upsell* directory of your own extension.
