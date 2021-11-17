These tasks are implemented as job controllers, PHP classes which can be executed from the command line or from a scheduler provided by the application.

# Location

The job implementations are grouped together, e.g. all administrative tasks are located in the "Admin" sub-directory of the *controller/jobs/src/Controller/Jobs* directory in the ai-controller-jobs extension. All order related jobs can be found in the "Order" sub-directory.

Depending on the type of task you need to implement, e.g if it depends on another one like the "product/export/sitemap" job controller, you may place your implementation in a sub-directory of one of the existing directories.

The first part of the job controller key (e.g. "product" in "product/export") corresponds to the domain of the managers in the *lib/mshoplib/src* directory of the Aimeos core. The term "domain" refers all classes that care about the same kind of data like the "order" domain for all order related data: Ordered products, customer addresses, used delivery and payment in orders and basic order information.

If you want to implement a job controller that mainly works with data from a domain like "media", you can create your controller in the directory *Controller/Jobs/Media* and then call it by pressing the "media/..." key.

# Factory

If you create a new job controller that doesn't extend an existing one, you need to implement a factory that cares about creating the job controller object. It will also wrap the decorators around if there are any configured. The factory only contains the static `create()` method with those few lines:

```php
namespace Aimeos\Controller\Jobs\Product\Export;

class Factory
    extends \Aimeos\Controller\Jobs\Common\Factory\Base
    implements \Aimeos\Controller\Jobs\Common\Factory\Iface
{
    public static function create( \Aimeos\MShop\Context\Item\Iface $context, \Aimeos\Bootstrap $aimeos, string $name = null ) : \Aimeos\Controller\Jobs\Iface
    {
        if( $name === null ) {
            $name = $context->getConfig()->get( 'controller/jobs/product/export/name', 'Standard' );
        }

        $iface = '\\Aimeos\\Controller\\Jobs\\Iface';
        $classname = '\\Aimeos\\Controller\\Jobs\\Product\\Export\\' . $name;

        if( ctype_alnum( $name ) === false ) {
            throw new \Aimeos\Controller\Jobs\Exception( sprintf( 'Invalid characters in class name "%1$s"', $classname ) );
        }

        $controller = self::createController( $context, $aimeos, $classname, $iface );

        return self::addControllerDecorators( $context, $aimeos, $controller, 'product/export' );
    }
}
```

The example is from the product export job controller. You need to replace all occurrences of "product", "Product", "export" and "Export" by the names that match your directories below *controller/jobs/src/Controller/Jobs/* in your Aimeos extension. If you want more than two levels, e.g. "product/export/sitemap", please extend the namespace, paths and class names by that last part.

# Skeleton

Creating a new job controller is rather simple because it needs to contain only three public methods:

```php
namespace Aimeos\Controller\Jobs\Product\Export;

class Standard
    extends \Aimeos\Controller\Jobs\Base
    implements Aimeos\Controller\Jobs\Iface
{
    public function getName() : string
    {
        return $this->getContext()->getI18n()->dt( 'controller/jobs', 'Product export' );
    }

     public function getDescription() : string
    {
        return $this->getContext()->getI18n()->dt( 'controller/jobs', 'Exports all available products' );
    }

     public function run()
    {
        // ...
    }
}
```

The name of the job controller corresponds to it's location in the file system. Each directory is a part of its name and the slashes (/) between the directory names are replaced by backslashes (\), so :

```
Controller/Jobs/Product/Export/Standard.php
```
maps to:
```
Aimeos\Controller\Jobs\Product\Export\Standard
```

For new implementations that are not an alternative to an existing implementation, you should always use "Standard" at the end to show that it is the standard implementation. This makes it easy to replace your implementation by an alternative one, e.g. *Aimeos\Controller\Jobs\Product\Export\Myexport* only by configuration.

Furthermore, you need to extend from the base abstract class *Aimeos\Controller\Jobs\Base* to have access to the context and to some helper methods for functionality that is commonly used. Finally, implementing the *Aimeos\Controller\Jobs\Iface* interface makes your class a job controller recognized by the core.

!!! warning
    Don't implement code in the constructor of the class that uses the context, e.g. for retrieving records from the database or logging something! To get the name and description of the job controller, the class is instantiated with a stripped down context object that doesn't contain the required services!

## getName()

To be able to show a name in the language of the shop owner instead of the key (e.g. "product/export") for your job controller, the `getName()` method should return a string that can be translated. This is done by the `dt()` method of the internationalization/translation object that is part of the context item:

```php
return $this->getContext()->getI18n()->dt( 'controller/jobs', 'Product export' );
```

There are several translation domains in the core but for job controllers you always need to use the "controller/jobs" translation domain as shown above. The second parameter of the `dt()` method is the name that should be translated, i.e. the name of your job controller in English.

## getDescription()

A more descriptive message about the functionality of your job controller should be returned by the `getDescription()` method. In order to be able to translate it to language of the shop owner, you have to use the `dt()` method of the internationalization/translation object:

```php
return $this->getContext()->getI18n()->dt( 'controller/jobs', 'Exports all available products' );
```

The translation domain is also "controller/jobs" like for the name. Descriptions should be short but descriptive enough so people not used to your job controller can understand what it does. Don't make it too long (more than 250 characters are to long for sure) because it depends on the application how the description is shown and there may be not enough space to display long texts.

## run()

All the real work is done by the `run()` method of your job controller. This method performs the tasks that your job controller is implemented for. Normally, it makes use of the Aimeos managers to retrieve, store or delete data in the storage, e.g.

```php
$manager = \Aimeos\MShop::create( $this->getContext(), 'product' );
$filter = $manager->filter()->add( 'product.type.code', '==', 'selection' );
$result = $manager->search( $filter, ['product', 'text'] );
```

The controller should not care about the used site as the defined by the cronjob. This also means that you don't have access to data across all shops but only to the data of the current site. Depending on the tasks your code has to do, you can alter the current language and currency in the site item stored in the context or set it to **null to get items of all languages and currencies**.

Working code for job controllers of different types can be found in the [controller/jobs/src/Controller/Jobs](https://github.com/aimeos/ai-controller-jobs/tree/master/controller/jobs/src/Controller/Jobs) directory of the core.

# Templates

You can use views and templates for generating output in job controllers. They are used in the same way as for the HTML clients, for example:

```php
$view = $this->getContext()->view();
$view->items = [1, 2, 3];

$tplconf = 'controller/jobs/product/export/template-items';
$default = 'product/export/items-body-default.xml';
$result = $view->render( $view->config( $tplconf, $default ) ) );
```

At first, you can retrieve a new view from the context object by using the `view()` method. For repeated calls it always returns a clean object regardless of what has been done with previous object. You can assign data directly like shown above or assign multiple key/value pairs at once using the `assign()` method. It's signature and more useful methods can be found in the [view class](https://github.com/aimeos/ai-controller-jobs/tree/master/controller/jobs/src/Controller/Jobs).

To render the output and return the content, you should use the `render()` method of the view. It expects the path of the template that should be used to generate the content. In combination with `$view->config()` it also checks if there's another template configured that should be used instead of the default one and translates a relative path into an absolute one.

The templates are looked up in the list of directories provided in the `"custom" => "controller/jobs/templates"` section of the manifest.php file that is part of every extension.

In the templates (usually in the sub-directories of "controller/jobs/templates"), the assigned data can be retrieved by using either:

```php
$this->varname
```
or:
```php
$this->get('varname', 'defaultvalue')
```

The later one is preferable because it returns a default value if the information is not available and doesn't throw an exception.

# Parallel processing

You can speed up jobs by splitting them into several independently running tasks. Thus, you can utilize multi-core systems efficiently for e.g. imports or exports. If you run several job controllers at once from a cron job, they are already automatically run in parallel if the system supports it.

It's also possible to e.g. read data from a file in chunks and process each chunk by a different task. For that, you need to create an anonymous function that will do the work after a new child process is spawned:

```php
$fcn = function( \Aimeos\MShop\Context\Item\Iface $context, $data ) {
    echo $data;
};

$context = $this->getContext()
$context->getProcess()
    ->start( $fcn, [$context, 'data1'] )
    ->start( $fcn, [$context, 'data2'] )
    ->wait();
```

This would span two child processes, both executing the anonymous function with a different data set. The result in this case can be "data1data2" or "data2data1", depending on which task completes first.

!!! warning
    The anonymous function should only operate on the non-shared arguments passed to the function (objects like the context are automatically cloned before they are passed). You must not facilitate more objects to the function via the `function() use( ... )` construct!

The **wait()** call cleans up the child processes after they have exited. You can also use it to wait for all running tasks before you start the next tasks using a different function for synchronization.

# Unit tests

Testing job controllers is an important part of the implementation to ensure that they are working correctly. The implementation of the unit tests cases doesn't differ much from other unit tests and you can use this skeleton for your own tests:

```php
namespace Aimeos\Controller\Jobs\Product\Export;

class StandardTest extends \PHPUnit\Framework\TestCase
{
    private $object;
    private $context;
    private $aimeos;

    protected function setUp() : void
    {
        \Aimeos\MShop::cache( true );

        $this->context = \TestHelperJobs::getContext();
        $this->aimeos = \TestHelperJobs::getAimeos();

        $this->object = new \Aimeos\Controller\Jobs\Product\Export\Standard( $this->context, $this->aimeos );
    }

    protected function tearDown() : void
    {
        \Aimeos\MShop::cache( false );
        unset( $this->object, $this->context, $this->aimeos );
    }

    public function testGetName()
    {
        $this->assertEquals( 'Product export', $this->object->getName() );
    }

    public function testGetDescription()
    {
        $text = 'Exports all available products';
        $this->assertEquals( $text, $this->object->getDescription() );
    }

    public function testRun()
    {
        $this->object->run();
        // test changes
    }
}
```

If you already know unit tests the implementation is pretty straight forward. The only thing that is special are these lines:

```php
\Aimeos\MShop::setCache( true );
\Aimeos\MShop::setCache( false );
```

When you use the `\Aimeos\MShop::create()` method to create manager objects, it caches objects and returns them if it's asked for the same kind of object again. In unit tests, this may have undesired side effects and therefore, the lines above enable this caching only for the test cases of this unit test class. At the end, it clears the object cache so the next unit test class starts in a clean state.

In this `testRun()` method, the tests should be looking for generated files or other changes. Often you may want to test if methods of objects used in the job controller are called. This is a bit more advanced as you must create mock objects first and let the `\Aimeos\MShop` class return them instead of creating a new, real object. An example would be:

```php
$mock = $this->getMockBuilder('\Aimeos\MShop\Product\Manager\Standard')
    ->setConstructorArgs( [$this->context] )
    ->setMethods( ['delete', 'save'] )
    ->getMock();

\Aimeos\MShop::inject( $this->context, 'product', $mock );

$mock->expects( $this->atLeastOnce() )->method( 'delete' );
$mock->expects( $this->atLeastOnce() )->method( 'save' );

$this->object->run();
```

This creates a product manager as mock object, injects it into the `\Aimeos\MShop` class and expects that the `delete()` and `save()` method has to be called at least once before the test is marked as successful.

More information about mocking object is available in the [test doubles section of PHPUnit](https://phpunit.de/manual/current/en/test-doubles.html).
