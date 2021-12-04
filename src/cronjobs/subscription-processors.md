When a customer has bought a product including a subscription interval, you can implement and configure additional tasks you need when the subscriptions begins, is renewed or ends. The article below describes how to implement your own subscription processor.

# Configure processors

These processors are included in the Aimeos core:

* [Cgroup](https://github.com/aimeos/ai-controller-jobs/blob/master/controller/common/src/Controller/Common/Subscription/Process/Processor/Cgroup/Standard.php)
: Add/remove user groups from customer account

* [Email](https://github.com/aimeos/ai-client-html/blob/master/controller/common/src/Controller/Common/Subscription/Process/Processor/Email/Standard.php)
: Send e-mails to customers if subscription renewal fails

By default, no processor is used by the subscription job controllers. To add the *Cgroup* processor for example, you have to use this configuration option:

```
controller/common/subscription/process/processors = ['Cgroup']
```

This setting requires an array of processor names that should be executed. Please refer to the articles about how to use configuration settings for your framework or application.

!!! warning
    The setting must be available when the job controller is executed. Thus, for TYPO3 it must be added to the TS-Config field of the scheduler task.

# Adapt existing processors

If you want to modify an existing processor implementation, e.g the *Cgroup* implementation that adds/removes groups to/from the customer, use the same directory but a different file/class name. The file  must be located in your own Aimeos extension:

```
./controller/common/src/Controller/Common/Subscription/Process/Processor/Cgroup/<name>.php
```

That class must extend from the existing class and only contain the methods you want to modifiy. For the *Cgroup* example and a file named *Mygroup.php* this can look like:

```php
namespace Aimeos\Controller\Common\Subscription\Process\Processor\Cgroup;

class Mygroup extends Standard
    implements \Aimeos\Controller\Common\Subscription\Process\Processor\Iface
{
    public function begin( \Aimeos\MShop\Subscription\Item\Iface $subscription )
    {
        // Your modifed code from the original method
    }
}
```

Afterwards, you have to configure your new *Mygroup* class so it's used instead of the *Standard* implementation. Use this configuration for the *Cgroup* example:

```
controller/common/subscription/process/processor/cgroup/name = Mygroup
```

The directory name *Cgroup* corresponds to the *cgroup* part of the configuration setting, i.e. the part in the configuration setting must be the lower case name of the directory part.

!!! warning
    The setting must be available when the job controller is executed. Thus, for TYPO3 it must be added to the TS-Config field of the scheduler task.

# Create new processors

To create a new subscription processor, the file for the class must be located in your own Aimeos extension in that directory structure:

```
./controller/common/src/Controller/Common/Subscription/Process/Processor/<name>/Standard.php
```

Please replace the "<type>" placeholder with the name of the task your processor handles, e.g. "Ldap" if it connects to an LDAP server to manage authorization information. The example below uses the type *Myproc*, so the file location in your own Aimeos extension would be:

```
./controller/common/src/Controller/Common/Subscription/Process/Processor/Myproc/Standard.php
```

Your new processor class should be used by the subscription job controllers and the appropriate method should be executed depending on the stage of the subscription. For that, you have to make your class known to the job controllers by adding this configuration option:

```
controller/common/subscription/process/processors = ['Myproc']
```

The code below contains a skeleton for the new class of type *Myproc*:

```php
namespace Aimeos\Controller\Common\Subscription\Process\Processor\Myproc;

class Standard
    extends \Aimeos\Controller\Common\Subscription\Process\Processor\Base
    implements \Aimeos\Controller\Common\Subscription\Process\Processor\Iface
{
    public function __construct( \Aimeos\MShop\Context\Item\Iface $context )
    {
        parent::__construct( $context );
        // more initialization code
    }

    public function begin( \Aimeos\MShop\Subscription\Item\Iface $subscription )
    {
        $context = $this->context();
        // Code that is executed at the beginning of the subscription
    }

    public function renewBefore( \Aimeos\MShop\Subscription\Item\Iface $subscription, \Aimeos\MShop\Order\Item\Iface $order )
    {
        $context = $this->context();
        // Code that is executed each time before the subscription is renewed
    }

    public function renewAfter( \Aimeos\MShop\Subscription\Item\Iface $subscription, \Aimeos\MShop\Order\Item\Iface $order )
    {
        $context = $this->context();
        // Code that is executed each time after the subscription is renewed
    }

    public function end( \Aimeos\MShop\Subscription\Item\Iface $subscription )
    {
        $context = $this->context();
        // Code that is executed at the end of the subscription
    }
}
```

You can remove each method you don't want to implement because there are default implementations available in the base class in this case.

Each method receives the [subscription item](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Subscription/Item/Iface.php) as first parameter. It contains the IDs of the original order and the subscription product. You can load the complete order using:

```php
$manager = \Aimeos\MShop::create( $context, 'order/base' );
$order = $manager->load( $subscription->getOrderBaseId() );
```

The `renew()` method also receives the new [order item](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Iface.php) that is created by job controller. You can use it to load the newly created order too:

```php
$manager = \Aimeos\MShop::create( $context, 'order/base' );
$order = $manager->load( $order->getBaseId() );
```

# Unit tests

Testing processors is an important part of the implementation to ensure that they are working correctly. The implementation of the unit tests cases doesn't differ much from other unit tests and you can use this skeleton for your own tests:

```php
namespace Aimeos\Controller\Common\Subscription\Process\Processor\Cgroup;

class StandardTest extends \PHPUnit\Framework\TestCase
{
    protected function setUp()
    {
        \Aimeos\MShop::cache( true );
    }

    protected function tearDown()
    {
        \Aimeos\MShop::cache( false );
    }

    public function testBegin()
    {
        $context = \TestHelperCntl::context();
        $manager = \Aimeos\MShop::create( $context, 'subscription' );
        $object = new \Aimeos\Controller\Common\Subscription\Process\Processor\Myproc\Standard( $context );
        $object->begin( $manager->create() );
    }
 }
```

If you already know unit tests the implementation is pretty straight forward. The only thing that is special are these lines:

```php
\Aimeos\MShop::cache( true );
\Aimeos\MShop::cache( false );
```

When you use the `\Aimeos\MShop::create()` method to create manager objects, it caches objects and returns them if it's asked for the same kind of object again. In unit tests, this may have undesired side effects and therefore, the lines above enable this caching only for the test cases of this unit test class and clears the object cache afterwards so the next unit test class starts in a defined state.

When testing subscription processor methods, it may be useful to test indirectly if the test case succeeded by testing what the method is doing internally, i.e. if object methods in the processor are called. This is a bit more advanced as you must create mock objects first and let the `\Aimeos\MShop` class return them instead of creating a new, real object:

```php
$customerStub = $this->getMockBuilder( '\\Aimeos\\MShop\\Customer\\Manager\\Standard' )
    ->setConstructorArgs( [$context] )
    ->setMethods( ['get', 'save'] )
    ->getMock();
\Aimeos\MShop::inject( $context, 'customer', $customerStub );

$customerStub->expects( $this->once() )->method( 'get' )
    ->will( $this->returnValue( $customerStub->create() ) );
$customerStub->expects( $this->once() )->method( 'save' );
```

This creates a customer manager as mock object, injects it into the `\Aimeos\MShop` class and defines that the `get()` and `save()` method has to be called at least once before the test is marked as successful.

More information about mocking object is available in the [test doubles section of PHPUnit](https://phpunit.de/manual/current/en/test-doubles.html).
