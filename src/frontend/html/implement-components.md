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

    public function getSubClient( string $type, string $name = null ) : \Aimeos\Client\Html\Iface
    {
        // optional
    }

    protected function getSubClientNames() : array
    {
        // optional
    }

    public function init()
    {
        // optional
    }

    public function modify()
    {
        // optional
    }

    public function data( Aimeos\MW\View\Iface $view, array &$tags = [], string &$expire = null ) : Aimeos\MW\View\Iface
    {
        // optional
    }
}
```

A component can implement the same optional methods as any subpart. For a detailed description of these methods, please refer to the article about [creating new subparts](create-subparts.md#optional-methods).

The [data()](create-subparts.md#data), [getSubClient()](create-subparts.md#getSubClient), [getSubClientNames()](create-subparts.md#getSubClientNames) and [modify()](create-subparts.md#modify) methods are also exactly the same as in any other subpart and won't be described in this article again.

Differences arise from the required code inside these methods as they have to care about caching (if you want to). Components that can cache its output are extremely fast. Once the content is generated and stored, it can be retrieved within milliseconds and directly pushed to the browser. The downside is that some additional code is needed.

# body()

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

# header()

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
