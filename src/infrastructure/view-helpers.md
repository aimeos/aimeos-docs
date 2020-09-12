The template views itself consist of HTML with [alternative PHP syntax](https://php.net/manual/en/control-structures.alternative-syntax.php). It's also possible to use the native template engine of your framework or application, i.e. Blade for Laravel, Twig for Symfony and Fluid for TYPO3. Please have a look at the "Get started" section to find out more.

To access the data assigned to the view, you can use:

```php
$this->get( 'somekey', [] ) // second parameter is the default value if not available
$this->somekey // throws an exception if not available
isset( $this->somekey ) // tests if the parameter is available
```

Additionally, there are some [view helpers](https://github.com/aimeos/aimeos-core/tree/master/lib/mwlib/src/MW/View/Helper) available. To use the view helpers in the view, call e.g.

```php
<?= $this->url( $target, $controller, $action, $params, $trailing, $config ) ?>
```

The example prints the generated URL for the given parameters. Use lower-case for all view helpers, i.e. "url()" for the view helper in the "Url" directory. The parameters for each view helper varies, so please have a look at each view helper you want to use.

# access

Tests if the current user is member of one of the given groups.

```php
<?php if( $this->access( ['mygroup', 'othergroup'] ) ) : ?>
  Yes, I'm a member!
<?php endif ?>
```

The parameter for the view helper can either be a single group name or a list of group names.

# block

Include subpart templates in your component templates. Contrary to partials, they are used by subparts, e.g. in that base template:

```html
<!-- parent template -->
<html>
  <head><title>Test template</title></head>
  <body>
<?= $this->block()->get( 'content' ) ?>
  </body>
</html>
```

You can include the output of this subpart template to create the full HTML page:

```html
<?php $this->block()->start( 'content' ) ?>
<!-- child template -->
<div class="test">
  <h1>Test</h1>
</div>
<?php $this->block()->stop(); ?>
```

# config

Access the configuration settings.

```php
<?= $this->config( 'client/html/catalog/detail/url/config', [] ) ?>
```

The first parameter is the configuration key, without slashes (/) at the beginning and the end. The second parameter is the default value, if no value is found in the configuration.

# content

Generates a URL from the paths which are stored in the database.

```php
<?= $this->content( 'relative/path/to/media.jpg' ) ?>
```

Depending on the environment and configuration, this view helper creates a

* local URL: "/data/relative/path/to/media.jpg"
* local absolute URL: "https://mydomain.com/data/relative/path/to/media.jpg"
* CDN link: "https://cdn.com/myshop/relative/path/to/media.jpg"
* data URL: "data:A0B1C2D3E4F5..."

# csrf

Secures form posts with a CSRF token.

```php
<?= $this->csrf()->formfield(); ?>
<?= $this->csrf()->name(); ?>
<?= $this->csrf()->value(); ?>
```

The *formfield()* method creates a hidden input field that can be added inside an HTML form tag, while the *name()* and *value()* methods return the single values for building an input field of your own.

# date

Translates a date into the localized format.

```php
<?= $this->date( '2000-01-01 00:00:00' ) ?>
```

The input must be an ISO date format in "YYYY-MM-DD HH:mm:ss" format.

# encoder

Quotes the data before printing it to avoid security breaches like cross site scripting (XSS).

```html
<input value="<?= $this->encoder()->attr( 'evil"value' ) ?>" />
<p><?= $this->encoder()->html( '<value>' ) ?></p>
<a href="<?= $this->encoder()->url( 'me & you?' ) ?>"></a>
<tag><?= $this->encoder()->xml( '<value>' ) ?></tag>
```

You have to use these methods all the time you output a non-static value and you must use the appropriate method for the context. Using *html()* for an attribute value will result in a XSS security hole!

# formparam

Generates the value for the "name" attribute of input elements. Depending on the environment, the value of the name attribute must be formatted differently. This method cares about the right value.

```php
<?= $this->formparam( 'name' ) ?> // as name=value in POST request
<?= $this->formparam( ['name', 'sub'] ) ?> // as name[sub]=value
<?= $this->formparam( ['name', ''] ) ?> // as name[]=value
```

If you forget to use the *formparam()* view helper, your component or subpart won't work in all frameworks or applications!

# imageset

Creates a string for the srcset attribute of image tags (`<image srcset="...">`) depending on the list of passed image widths and URLs used for response images.

```php
<?= $this->imageset( [100 => '/path/to/100width.jpg', 300 => '/path/to/300width.jpg'] ) ?>
```

This will generate a string of `/path/to/100width.jpg 100w, /path/to/300width.jpg 300w`.

# link

Generates a URL for the `url` configuration key, parameters and anchor fragments.

```php
<?= $this->link( 'client/html/catalog/detail/url', ['d_prodid' => 1], ['image', '2'] ) ?>
```

The first argument is the common prefix for:

* client/html/catalog/detail/url/target
* client/html/catalog/detail/url/controller
* client/html/catalog/detail/url/action
* client/html/catalog/detail/url/config
* client/html/catalog/detail/url/filter

The second one contains the parameters that should be part of the URL and the third are the fragments that creates the anchor links.

# mail

Provides access to an e-mail message that can be filled with a message body.

```php
<?php $message = $this->mail(); ?>
```

The available methods in the message object are available in the [Aimeos\MW\Mail\Message\Iface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Mail/Message/Iface.php).

# number

Returns the localized integer or decimal value for the given number.

```php
<?= $this->number( 123 ) ?> // 123.00
<?= $this->number( 123.45, 1 ) ?> // 123.4
```

The second parameter is the number of decimal digits the result should contain. Depending on the locale settings, the decimal point and the thousand separator are different.

# param

Returns the  GET/POST/URL parameter or a list if it's an array.

```php
<?= $this->param( 'myparam' ) ?>
<?= $this->param( 'myparam', 'default' ) ?>
```

The first argument is the name of the parameter, the second argument is the default value if no value was found (or null if not used).

Also, the first argument can be a path to the value separated by slashes (/) in case it's a multi-dimensional array:

```php
// parameter structure: ['my' => ['param' => 'value']]
<?= $this->param( 'my/param' ) ?>
```

This would return 'value'.

# partial

Renders the given sub-template with the arguments passed.

```php
<?= $this->partial( 'mytemplate.php', ['key' => 'value'] ) ?>
```

The path of the template must be relative to the "templates" directory.

# request

Returns the request object implementing the PSR-7 ServerRequestInterface.

```php
<?php $request = $this->request(); ?>
```

For more information about PSR-7 requests, please have a look into the [PHP-FIG documentation of the PSR-7 standard](https://www.php-fig.org/psr/psr-7/).

# response

Returns the response object implementing the PSR-7 ResponseInterface.

```php
<?php $response = $this->response(); ?>
```

For more information about PSR-7 requests, please have a look into the [PHP-FIG documentation of the PSR-7 standard](https://www.php-fig.org/psr/psr-7/).

# session

Returns the value stored in the session of the user.

```php
<?php echo $this->session( 'a/session/key', 'mydefault' ) ?>
```

The first parameter is the session key which was used to store the value in the session of the user. The key can be any string but using characters, numbers and slashes is recommended. The second parameter is the value returned if the key isn't available in the session.

# translate

Translates a string according to the current locale.

```php
<?php echo $this->translate( 'client/code', 'size' ) ?>
<?php echo $this->translate( 'client', '%1$d article', '%1$d articles', 10 ) ?>
```

The first form is for singular translations, the second one for plural ones.

# url

Generates URLs for the given target, controller, action, parameter and configuration.

```php
$target = $this->config( 'client/html/catalog/detail/url/target' );
$controller = $this->config( 'client/html/catalog/detail/url/controller', 'catalog' );
$action = $this->config( 'client/html/catalog/detail/url/action', 'detail' );
$config = $this->config( 'client/html/catalog/detail/url/config', [] );
$trailing = ['anchor']; // will be added as #anchor
$params = ['d_prodid' => 1];

echo $this->url( $target, $controller, $action, $params, $trailing, $config );
```

Besides the parameter and the trailing array, all other arguments should be retrieved from the configuration.

# value

Returns a value from a multi-dimensional arrays in a simple way.

```php
<?php echo $this->value( $array, 'path/to/key' ) ?>
<?php echo $this->value( $array, 'path/to/key', 'default' ) ?>
```

The first argument is the array and the second one the path to the value separated by slashes (/). The second parameter of the method is the default value returned if no value was found (or null if not used).

The examples assume an array structure like this one.

```
['path' => ['to' => ['key' => 'value']]]
```

and then, the view helper would return *value*.
