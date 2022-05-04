# Create extension

Aimeos and the Aimeos TYPO3 extension are very powerful, but there are numerous features that are only available through additional extensions. Often, your project also requires special features that makes it different from other web sites build with Aimeos.

But extending the Aimeos TYPO3 extension itself is a bad thing, because you will loose the ability to update the extension. To solve this, the Aimeos TYPO3 extension allows you to integrate your own TYPO3 extension containing additional Aimeos extensions.

!!! tip
    You can easily create a new extension that is already packaged inside a TYPO3 extension using the [extension generator](https://aimeos.org/extensions/)

# Aimeos objects

If you need to instantiate the Aimeos controllers or managers directly in your TYPO3 extension and call their methods, you have to supply a [context object](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/ContextIface.php). This object is a dependency injection container that offers access to configuration settings, database connections, session and content cache as well as translation facilities. You can get an instance in TYPO3 depending on your environment:

```php
// in a controller action
use Aimeos\Aimeos\Controller\AbstractController;

class YourController extends AbstractController
{
    public function indexAction() {
        $context = $this->contex();
    }
}

// in a scheduler task
$context = \Aimeos\Aimeos\Scheduler\Base::contex( $localConfigArray );

// anywhere else
$config = \Aimeos\Aimeos\Base::config( $localConfigArray );
$context = \Aimeos\Aimeos\Base::contex( $config );
```

In the MVC controller actions, where the required parameters for site, language and currency are available as part of the request, a locale object is added to the context automatically. Everywhere else, you need to retrieve this values from somewhere else, e.g. the configuration. Then, you can use the *bootstrap()* method of the [locale manager](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Locale/Manager/Iface.php) to retrieve the locale item yourself:

```php
$manager = \Aimeos\MShop::create( $context, 'locale' );
$item = $manager->bootstrap( '<sitecode>', '<languageid>', '<currencyid>', true );
$context->setLocale( $item );
```

The language and currency IDs are optional and the first matching locale item from the *mshop_locale* table in the database will be used. If there are no entries in the *mshop_locale* table, because you want to manage the data in a custom administration interface, you can create an empty locale object yourself:

```php
$manager = \Aimeos\MShop::create( $context, 'locale' );
$item = $manager->create()->setLanguageId( 'en' );
$context->setLocale( $item );
```

It's a good idea to set at least the currently used language ID because then you are able to add the translation facilities for this language, too, and there won't be any exceptions, if some code wants to translate a string:

```php
// use the appropriate way depending on your environment
$context->setI18n( \Aimeos\Aimeos\Base::getI18n( ['en'] ) );
```

Alternatively, if you don't want any translation, you can add a "Null" object instead. It returns the singular or plural string untranslated, and for this decision it needs the language ID to determine the right singular/plural rule:

```php
$context->setI18n( ['en' => new \Aimeos\MW\Translation\None()] );
```

Afterwards, you are able to create every object from the Aimeos core and save, retrieve or delete the stored data. You should never use the "new" operator to create a new object, because the implementation variant depends on the configuration and decorators are added automatically. Instead, use the *Aimeos\MShop* class or any more specific factory to create new objects, e.g.

```php
$manager = \Aimeos\MShop::create( $context, 'product' );
$filter = $manager->filter()->add( 'product.code', '==', 'test' );

foreach( $manager->search( $filter ) as $id => $item ) {
    // print_r( $item );
}
```

# Bootstrap code

It's the Aimeos concept that you can overwrite anything and adapt it to your needs. Thus, you can also replace almost every single piece of code that builds the TYPO3 environment for the Aimeos core.

## Base classes

Aimeos requires a few classes that are necessary for bootstrapping. They include:

* *\Aimeos\Aimeos\Base\Aimeos* (Core bootstrapping)
* *\Aimeos\Aimeos\Base\Config* (Configuration settings)
* *\Aimeos\Aimeos\Base\Context* (Dependency container)
* *\Aimeos\Aimeos\Base\I18n* (Translation and internationalization)
* *\Aimeos\Aimeos\Base\Locale* (Site, language and currency setup)
* *\Aimeos\Aimeos\Base\View* (Template engine setup)

You can find these classes in the *./Classes/Base/* directory of the [Aimeos TYPO3 extension](https://github.com/aimeos/aimeos-typo3/tree/master/Classes/Base). To overwrite their code, you should create your own class and extend from the original one if necessary. Afterwards, you need to configure the name of your new class in the `ext_localconf.php` file, e.g.

```php
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view'] = 'Myview';
```

You can use that kind of statements for all classes you want to overwrite:

```php
// core bootstrapping
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos'] = '...';
// configuration settings
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_config'] = '...';
// dependency container
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context'] = '...';
// translation and internationalization
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_i18n'] = '...';
// site, language and currency setup
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_locale'] = '...';
// Template engine setup
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view'] = '...';
```

To add a new view helper you've implemented (requiring a TYPO3 object) to the view object for example, you can add this to the `ext_localconf.php` of your own TYPO3 extension:

```php
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view'] =
    function( \Aimeos\MShop\Context\Item\Iface $context,
        \TYPO3\CMS\Extbase\Mvc\Web\Routing\UriBuilder $uriBuilder, array $templatePaths,
        \TYPO3\CMS\Extbase\Mvc\RequestInterface $request = null, $langid = null
    ) {
        $view = \Aimeos\Aimeos\Base\View::get( $context, $uriBuilder, $templatePaths, $request, $langid );
        $service = \TYPO3\CMS\Core\Utility\GeneralUtility::makeInstance( 'ImageService' );
        $helper = new \Aimeos\MW\View\Helper\Request\ImageService( $view, $service );
        $view->addHelper( 'imageservice', $helper );
        return $view;
}
```

## Dependency container

The context class itself contains a lot of objects that are used by the Aimeos core to interact with TYPO3 or abstract from a concrete implementation. Those objects are:

* Cache
* Database
* File system
* Logging
* Mail client
* Message queue
* Passwort hashing
* Session
* User
* User groups

Please have a look into the default implementation of the [context object setup](https://github.com/aimeos/aimeos-typo3/blob/master/Classes/Base/Context.php) to get a feeling for the necessary tasks. You can overwrite any injected object into the context by configuring your own anonymous function in the `ext_localconf.php` file:

```php
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_logger'] =
    function( \Aimeos\MShop\Context\Item\Iface $context )
    {
        $loglevel = \Aimeos\MW\Logger\Base::DEBUG;
        $logger = new \Aimeos\MW\Logger\File( '/tmp/aimeos.log', $loglevel );

        return $context->setLogger( $logger );
    };
```

Your anonymous function receives the current context object, needs to set the new object you've created and returns the context object again. This works in the same way for all dependencies:

```php
// Cache infrastructure
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_cache'] = ...
// Database abstraction
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_dbm'] = ...
// File system abstraction
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_fsm'] = ...
// Password hashing algorithm
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_hasher'] = ...
// Logging facility
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_logger'] = ...
// Sending e-mails
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_mailer'] = ...
// Message queue
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_mqueue'] = ...
// Common session
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_session'] = ...
// Authenticated user
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_user'] = ...
// Groups the user is in
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_groups'] = ...
```

## View helper

In the same way as for the context object, you can use your own anonymous functions to overwrite the view helpers added to the Aimeos template engine. View helpers added by default are:

* Group based access control
* Configuration settings
* Form parameter naming
* Number format
* Parameter retrieval
* Request object access
* Response object access
* Translation and internationalization
* URL generation

The default implementation reveals the details of the [view object setup](https://github.com/aimeos/aimeos-typo3/blob/master/Classes/Base/View.php) so you can change it according to your needs. Replacing a view helper is done by adding the configuration to the `ext_localconf.php` file for your anonymous function:

```php
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_access'] =
    function( \Aimeos\MW\View\Iface $view )
    {
        $helper = new \Aimeos\MW\View\Helper\Access\All( $view );
        return $view->addHelper( 'access', $helper );
    };
```

Your anonymous function receives at least the current view object, needs to add the new object you've created and returns the view object again. Depending on the view helper, more than one argument is passed to your anonymous function. You can check in the [default implementation](https://github.com/aimeos/aimeos-typo3/blob/master/Classes/Base/View.php) if this is the case.

You can do this In the same way for all other view helpers:

```php
// Group based access control
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_access'] = ...
// Configuration settings
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_config'] = ...
// Form parameter naming
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_formparam'] = ...
// Number format
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_number'] = ...
// Parameter retrieval
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_param'] = ...
// Request object access
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_request'] = ...
// Response object access
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_response'] = ...
// Translation and internationalization
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_translate'] = ...
// URL generation
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_view_url'] = ...
```

# Change logging

You can change logging from the database to another target in  `ext_localconf.php`, e.g.:

```php
$GLOBALS['TYPO3_CONF_VARS']['EXTCONF']['aimeos']['aimeos_context_logger'] = function( $context ) {
    return $context->setLogger( new \Aimeos\MW\Logger\File( '/path/to/file', <loglevel>, [<facility>] ) );
}
```

The *loglevel* parameter is the minium level for which messages get logged, e.g. a log level of "3" logs all "error", "critical" and "alert" and "emergency" messages. The available log levels are:

* 0: Emergency
* 1: Alert
* 2: Critical
* 3: Error
* 4: Warning
* 5: Notice
* 6: Info
* 7: Debug

The "facility" parameter limits the log messages to the list of given facilities, the names of the sources of the log messages, e.g. "core/sql". If no paramter or *null* is passed, all error messages are logged.

The available logger implementations are:

* File( $filename, $priority = \Aimeos\MW\Logger\Base::ERR, array $facilities = null )
* Errorlog( $loglevel = \Aimeos\MW\Logger\Base::ERR, array $facilities = null )
* Compose( array $loggers )

The *Compose* logger can send log messages to different loggers, e.g. to the *File* logger and a self written logger:

```php
new \Aimeos\MW\Logger\Compose( [
    new \Aimeos\MW\Logger\File( '/path/to/file' ),
    new \Aimeos\MW\Logger\MySmsLogger( '<number>', 2 ),
] );
```

This would log all error/critical/alert/emergency messages to the given file and send a SMS for all critical/alert/emergency messages.
