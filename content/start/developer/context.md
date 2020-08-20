The [context item](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Context/Item/Iface.php) is the dependency container of Aimeos and gives you access to the host system, independent of the used framework or application. It's available in all classes of the [data access layer and above](architecture.md) except the items (and template files of course) by calling

```php
$this->getContext()
```

# Cache

The caching framework can store arbitrary pairs of key/value and should be used to share content between requests and servers. It's not guaranteed that the cached data is available at all because the cache can be purged at any time. The content cache must be used with a fallback strategy if the cached item isn't available.

``` php
$cache = $this->getContext()->getCache()
    ->set( 'myuniquekey', 'some content' )
    ->get( 'myuniquekey' );
```

The full description of its methods is available in the documentation of the [cache interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Cache/Iface.php).

# Configuration

All configured settings are available in the config object and can be retrieved via their unique keys. These keys are built hierarchically and their parts are separated by slashes. The hierarchy matches the nested configuration arrays which can map to the configuration files in the config directories.

```php
$config = $this->getContext()->getConfig()
    ->get( 'client/html/catalog/detail/standard/subparts', [] );
```

The full description of its methods is available in the documentation of the [config interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Config/Iface.php).

# Database

By using the database manager, you can get access the configured database connections and can retrieve or manipulate records.

!!! note
    Don't use the database connection to manipulate records that are managed by Aimeos! These can be inserted, fetched, updated and deleted in a save and comfortable way by the Aimeos managers.

First you have to get the correct connection and release it again after you are done:

```php
$dbm = $this->getContext()->getDatabaseManager();
$conn = $dbm->acquire( 'db-product' );
$conn->begin();

try {
    // ...
    $conn->commit();
} catch( \Exception $e ) {
    $conn->rollback();
} finally {
    $dbm->release( $conn, 'db-product' );
}
```

!!! warning
    It's extremely important that you release the database connection again using the same name as in *acquire()* because it's shared within the process. If you forget to do this, new connections will be opened until the connection limit is reached and an exception is thrown!

With the connection object, you can execte a SQL statement:

```php
$stmt = $conn->create( 'UPDATE "mytable" SET "mycol" = ? WHERE "myid"=?' )
    ->bind( 1, 'some value' );
    ->bind( 2, 123, \Aimeos\MW\DB\Statement\Base::PARAM_INT );
    ->execute()
	->finish();
```

To retrieve data, you have to fetch the data of the result set:

```php
$result = $conn->create( 'SELECT * FROM "mytable" WHERE "mycol" = ?' )
    ->bind( 1, 'myvalue' )
	->execute();

while( $row = $result->fetch() ) {
    // $row is an associative array of column names and values
}
```

!!! warning
    You have to **fetch all rows** returned by the result set! If not, the leftover rows will be returned as part of the next result set. Supposed you only need the first row, you can throw away all others by calling *$result->finish()*.

For detailed information about the available methods, please have a look into these interfaces:

* [database manager](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/DB/Manager/Iface.php)
* [connections](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/DB/Connection/Iface.php)
* [statements](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/DB/Statement/Iface.php)
* [result sets](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/DB/Result/Iface.php)

# File system

The file system object gives you access to the configured parts of the storage. This may be the local file system but can be a remote FTP server or the AWS cloud too, depending on the configuration. You doesn't have to care about the details because the file system interface provides a way to work with any storage the same way.

```php
$fs = $this->getContext()->getFileSystem( 'fs-secure' );
$fs->write( 'somefile.txt', 'some content' );
$content = $fs->read( 'somefile.txt' );
```

If directories are supported, you can create or delete them too:

```php
if( $fs instanceof \Aimeos\MW\Filesystem\DirIface )
{
    if( !$fs->isDir( 'mydir' ) ) {
        $fs->mkdir( 'mydir' );
    }
    $fs->write( 'mydir/somefile.txt', 'some content' );
}
```

Some file systems also support file meta data:

```php
if( $fs instanceof \Aimeos\MW\Filesystem\MetaIface ) {
    $size = $fs->size( 'myfile.txt' );
}
```

For detailed information about the available methods, please have a look into these interfaces:

* [file system](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Filesystem/Iface.php)
* [directories](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Filesystem/DirIface.php)
* [meta data](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Filesystem/MetaIface.php)

# I18n (Translation)

To enable translation of strings to other languages than English, you should use he "i18n" (internationalization) object. You can translate both, singular and plural strings.

```php
$i18n = $this->getContext()->getI18n();
$str = $i18n->dt( 'client', 'One string' );
$str = sprintf( $i18n->dn( 'client', 'One string', '%1$d strings', 5 ), 5 );
```

More information about the methods is available in the [translation interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Translation/Iface.php).

# Locale

The locale object contains the current site object including the site ID and the configuration key/value pairs for this site. Additionally, when created for the front-end it also contains the language and currency ID that should be used to filter language and currency specific data. In the backend, both values will be null.

```php
$locale = $this->getContext()->getLocale();
$languageid = $locale->getLanguageId();
$currencyid = $locale->getCurrencyId();
$site = $locale->getSite();
```

More information about the methods is available in the [locale interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Locale/Item/Iface.php).

# Logger

Writing log entries is essential for reporting unexpected behavior. The logger object abstracts from the concrete log implementation, so you don't have to care about the details. By default, the *log()* method will write entries of priority "error" to the "message" facility. Depending on the log configuration, only log messages with priorities equal or higher to the one will be written to the log. Thus, on a development vhost a priority of "debug" makes sense, while on the production server it should be limited to "warning" or "notice". The facility can be used to log into different locations.

```php
$logger = $this->getContext()->getLogger()
    ->log( 'payment failed', \Aimeos\MW\Logger\Base::WARN, 'payment' )
    ->log( 'some message' );
```

More information about the methods is available in the [logger interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Logger/Iface.php). The constants for the second parameter are listed in the [logger base class](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Logger/Base.php).

# Mail

Sometimes, you will need to send an e-mail to someone for notification. The mail object offers a simple but yet powerful interface to the mail implementation of the host framework or application and its configuration. It's much more flexible than the PHP *mail()* function.

```php
$this->getContext()->getMail()
    ->createMessage()
    ->addFrom( 'me@localhost' )
	->addTo( 'me@example.com' )
    ->setSubject( 'Important message' )
    ->setBody( 'The text body' )
    ->addAttachment( 'some data', 'text/plain', 'myfile.txt' )
    ->send();
```

For detailed information about the available methods, please have a look into these interfaces:
* [mail interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Mail/Iface.php)
* [message interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Mail/Message/Iface.php)

# Message queues

If a request requires to do some tasks in the background, you can send it to a message queue and process it later. This prevents your request to run into the PHP memory or execution time limit and can be used to offload resource intensive tasks to other servers. A message queue is only a place where job descriptions can be temporarily stored, so you have to implement a [job controller](../../cronjobs/create-job-controller.md) too that processes the job.

To add a new job to the message queue "mq-email" configured in the resource configuration:

```php
$queue = $this->getContext()
    ->getMessageQueue( 'mq-email', 'order/email/payment' )
    >add( json_encode( ['email' => 'me@example.com'] ) );
```

The second parameter can be any string, it's only important to know for the job controller:

```php
$queue = $this->getContext()
    ->getMessageQueue( 'mq-email', 'order/email/payment' );

while( $msg = $queue->get() )
{
    $data = json_decode( $msg->getBody() );
    // perform the task
    $queue->del( $msg );
}
```

More information about the available methods is available in the [message queue interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/MQueue/Queue/Iface.php).

!!! waring
    It's important to delete the message you've processed in the job controller afterwards! Otherwise, the message will be processed over and over again and will utilize all resources of the server.

# Parallel processing

Aimeos offers the necessary infrastructure for processing tasks in parallel und therefore utilizing multi-core architectures of CPUs efficiently. This is only available in [job controllers](../../cronjobs/create-job-controller.md) executed from the command line e.g. via scheduled cron jobs.

```php
$fcn = function( \Aimeos\MShop\Context\Item\Iface $context, $data ) {
    echo $data;
};

$context = $this->getContext()
$context->getProcess();
    ->start( $fcn, [$context, 'data1'] )
    ->start( $fcn, [$context, 'data2'] )
    ->wait();
```

You can call *start()* as many times as you need. The process implementation cares about executing the passed anonymous function without overloading the server. The list of arguments in the second parameter are passed to your anonymous function in the same order. At last, you have to call *wait()* which will return when all running jobs are completed.

Please have a look at the [article about parallel processing](../../cronjobs/create-job-controller.md#Parallel-processing) too.

# Session

If you need to store information about the users and retrieve it at a later request, you can utilize their user session for temporarily saving that information.

```php
$session = $this->getContext()->getSession();
$session->set( 'myprefix/myvalue', 'some value' );
$session->get( 'myprefix/myvalue' );
```

Details about the methods are available in the [session interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Session/Iface.php).

# Template view

The view object is a powerful way to render HTML for the front-end, XML for exports and content for e-mails. It encapsulates a complete template engine and offers view helpers for the most often used tasks. Depending on the framework or application, additionally to the Aimeos PHP template engine you have Blade in Laravel, Twig in Symfony and Fluid in TYPO3/Flow available.

```php
$view = $this->getContext()->getView();
$view->myvalue = 'some value';
$content = $view->render( 'path/to/template.php' ); // Aimeos PHP
$content = $view->render( 'path/to/template.blade.php' ); // Laravel
$content = $view->render( 'path/to/template.html.twig' ); // Symfony
$content = $view->render( 'path/to/template.html' ); // TYPO3/Flow
```

The path of the templates is relative to the [configured directory in the manifest.php of you extension](extensions#custom). Within the templates, you have access to all assigned data (e.g. "myvalue") and all view helpers. The view helpers are different if you use Blade, Twig or Fluid.

```php
<?= $this->get( 'myvalue', 'default value' ) ?>
<?= $this->number( 123.45 ) ?>
```

Details about the view methods and a list of view helpers is available in the [documentation of the view interface](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/View/Iface.php).

# Editor

The account name of the current user/editor or IP address if the user isn't logged in is available via

```php
$this->getContext()->getEditor();
```

# User ID

The ID of the current user/editor is available via

```php
$this->getContext()->getUserId();
```

If the user isn't logged in, null is returned instead.

# Group IDs

The IDs of the groups the current user/editor is in is available via

```php
$this->getContext()->getGroupIds();
```

If the user isn't logged in, an empty array is returned instead.
