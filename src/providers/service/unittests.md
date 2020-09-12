Testing is an essential part of software development. Unit tests can execute test cases automatically and will save you a lot of time by avoiding manual tests after changes. They uncover programming and logical errors by executing the code paths so your goal should be to have a code coverage of at least 90% and test most of your code paths.

Test classes are located in the *./test/* directory next to the *./src/* directory and use the same directory structure as in the *./src/* directory. The test class file itself is named like the original file but with "Test" at the end, e.g. if your service provider class file is named "Myprovider.php" then the test class file must be named "MyproviderTest.php".

!!! tip
    For a basic understanding of unit tests in PHP, please read the [documentation of PHPUnit](https://phpunit.de/manual/current/en/index.html) first!

# Test setup

A test class for service providers needs a *setUp()* method to create an object you can run your tests against. This method is executed before every test method so you have a clean object in each test. A basic skeleton of a test class will look like this:

```php
namespace Aimeos\MShop\Service\Provider\Payment;

class MyproviderTest extends \PHPUnit_Framework_TestCase
{
    private $object;
    private $serviceItem;


    protected function setUp()
    {
        $context = TestHelperMShop::getContext();

        $serviceManager = Aimeos\MShop\Factory::createManager( $context, 'service' );
        $this->serviceItem = $serviceManager->createItem();

        $this->object = $this->getMockBuilder( 'Aimeos\MShop\Service\Provider\Payment\Myprovider' )
            ->setMethods( ['getOrder', 'getOrderBase', 'saveOrder', 'saveOrderBase', 'myConnection'] )
            ->setConstructorArgs( [$context, $this->serviceItem] )
            ->getMock();
    }
}
```
To ease testing, you shouldn't instantiate your service provider directly. Instead, use the *getMockBuilder()* method to create an object where several methods are overwritten, especially those that would interact with the database to retrieve or save orders. This avoids changing test data in the database and allows you to control the program flow.

!!! tip
    For easier testing you must move the code that interacts with any remote service to its own method! Thus, you can replace that method in your tests with a stub and are not dependent on the availability of the remote gateway.


The *setMethods()* call contains the methods that will be replaced by stubs. In the example above, this also contains a method named *myConnection()* which should be replaced by the name of your method that handles the interaction with the remote gateway.

# Supporting method

In the test methods you often need an order item but not in all. It would be too expensive to fetch an item from the database in *setUp()* for every test method even if it isn't needed. Therefore, the examples below use this support method to retrieve an item only when it's necessary:

```php
protected function getOrderItem()
{
    $manager = \Aimeos\MShop\Factory::createManager( TestHelperMShop::getContext(), 'order' );

    $search = $manager->createSearch();
    $search->setConditions( $search->compare( '==', 'order.datepayment', '2008-02-15 12:34:56' ) );

    $result = $manager->searchItems( $search );

    if( ( $item = reset( $result ) ) === false ) {
        throw new Exception( 'No order found' );
    }

    return $item;
}
```

It simply returns one specific order item from the unit test dataset.

# Get front-end / back-end configuration

If you have configured some front-end or back-end configuration, testing is really simple. You only have to check if the returned result matches your expectations:

```php
public function testGetConfigBE()
{
    $result = $this->object->getConfigBE();

    $this->assertInternalType( 'array', $result );
    $this->assertArrayHasKey( 'myprovider.mykey', $result );

    foreach( $result as $attr ) {
        $this->assertInstanceOf( '\Aimeos\MW\Criteria\Attribute\Iface', $attr );
    }
}
```

The output of the *getConfigBE()* and *getConfigFE()* methods must be an array of *Aimeos\MW\Criteria\Attribute\Iface* objects with the keys defined in your service provider. You should check if every key is available by using the *assertArrayHasKey()* method.

# Check front-end / back-end configuration

To check the entered configuration values, the *checkConfigBE()* and *checkConfigFE()* methods are used. They are tested in a very similary way than the *getConfigBE()* and *getConfigFE()* methods.

```php
public function testCheckConfigBE()
{
    $result = $this->object->checkConfigBE( ['myprovider.mykey' => 'myvalue'] );

    $this->assertEquals( 1, count( $result ) );
    $this->assertNull( $result['myprovider.mykey'] );
}
```

Testing them requires passing some test values for the available keys to the methods. You should test for all your keys and pass invalid test data too so you can see if the methods behave as expected.

# Check optional methods

There are some optional methods like *cancel()*, *capture()*, *query()* and *refund()* that don't have to be implemented. If one of these methods is available, you also need to check if *isImplemented()* returns the correct value:

```php
public function testIsImplemented()
{
    $this->assertTrue( $object->isImplemented( \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_CANCEL ) );
    $this->assertTrue( $object->isImplemented( \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_CAPTURE ) );
    $this->assertTrue( $object->isImplemented( \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_QUERY ) );
    $this->assertTrue( $object->isImplemented( \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_REFUND ) );
}
```

The *isimplemented()* method must return true for every optional methods that is available in your service provider and false for all others.

# Test payment processing

The heart of every service provider is the *process()* method and it's important to test it thoroughly. Depending on the way it handles the payment (collect locally, redirect to the payment gateway, send data to a remote API or a combination thereof), you have to write several tests to cover each code path.

```php
public function testProcess()
{
    // ...

    $this->object->expects( $this->once() )->method( 'myConnection' );

    $result = $this->object->process( $this->getOrderItem(), [] );

    $this->assertInstanceOf( '\Aimeos\MShop\Common\Item\Helper\Form\Iface', $result );
}
```

This test example covers the two assertions that will be most often required: Check if the remote service would be contacted and test if the returned object is a form helper object. You should add more assertions and expectations depending on your code.

# Direct status update

Testing direct status updates involves retrieving the order and saving the modified order back to the database. To decouple the test from the database so no test data will be changed, you should make use of the stubbed *saveOrder()* method.

```php
public function testUpdateSync()
{
    $psr7request = $this->getMockBuilder( '\Psr\Http\Message\ServerRequestInterface' )->getMock();

    $psr7request->expects( $this->once() )->method( 'getQueryParams' )
        ->will( $this->returnValue( ['key' => 'value'] ) );

    $this->object->expects( $this->once() )->method( 'saveOrder' );

    $result = $this->object->updateSync( $psr7request, $this->getOrderItem() );

    $this->assertInstanceOf( '\Aimeos\MShop\Order\Item\Iface', $result );
    $this->assertEquals( \Aimeos\MShop\Order\Item\Base::PAY_RECEIVED );
}
```

You can tell the stubbed methods to return a value of your choice, e.g. the required GET parameter. The expectation for *saveOrder()* will test if the method is called but won't change anything in the database.

# Notification status update

Testing status updates sent via notification requests requires working with PSR-7 request and response objects. Also, you need to stub the *saveOrder()* method like for direct status update to prevent changing the test data in the database.

```php
public function testUpdateSync()
{
    $psr7stream = $this->getMockBuilder( '\Psr\Http\Message\StreamInterface' )->getMock();
    $psr7request = $this->getMockBuilder( '\Psr\Http\Message\ServerRequestInterface' )->getMock();
    $psr7response = $this->getMockBuilder( '\Aimeos\MW\View\Helper\Response\Iface' )->getMock();

    $psr7request->expects( $this->once() )->method( 'getQueryParams' )
        ->will( $this->returnValue( ['key' => 'value'] ) );

    $psr7response->expects( $this->once() )->method( 'withBody' )
        ->will( $this->returnValue( $psr7response ) );

    $psr7response->expects( $this->once() )->method( 'withHeader' )
        ->will( $this->returnValue( $psr7response ) );

    $psr7response->expects( $this->once() )->method( 'createStreamFromString' )
        ->will( $this->returnValue( $psr7stream ) );

    $result = $this->object->updatePush( $psr7request, $psr7response );

    $this->assertInstanceOf( '\Psr\Http\Message\ResponseInterface', $result );
}
```

When stubbing PSR-7 objects, you have to make sure that all methods changing the state of the object will return the (modified) object again! In this example, this the case for *withBody()* and *withHeader()* if you use them in your payment provider. The *createStreamFromString()* method is an addition in Aimeos to prevent being dependent on a concrete stream implementation. The expectation for *saveOrder()* will test if the method is called but won't change anything in the database.

# Batch status update

For batch updates, the test case is very similar to that of the *updateSync()* method. You will need to provide the test data and if there's a test file, you can configure its location in the used service item.

```php
public function testUpdateAsync()
{
    // ...

    $this->serviceItem()->setConfig( array( /* ... */ ) );

    $this->object->expects( $this->atLeastOnce() )->method( 'getOrder' )
        ->will( $this->returnValue( $this->getOrderItem() ) );
    $this->object->expects( $this->atLeastOnce() )->method( 'saveOrder' );

    $result = $this->object->updateAsync();
}
```

The rest of the test case is much like in the *updateSync()* method to prevent changes in the database. Depending on how much data is in your test file, the *getOrder()* and *saveOrder()* methods will be called more than once which is covered by the *atLeastOnce()* expectation.

# Test optional methods

All optional methods (*cancel()*, *capture()* and *refund()* for payment service provider, *query()* for both, delivery and payment service providers) can be tested in the same way because their method signature is the same, and they all behave in a very similar way: Use the ID of the given order to connect to a remove gateway and update the delivery or payment status afterwards:

```php
public function testCancel()
{
    // ...

    $this->object->expects( $this->once() )->method( 'myConnection' );
    $this->object->expects( $this->once() )->method( 'saveOrder' );

    $this->object->cancel( $this->getOrder() );
}
```

You only need to make sure that your expectations (connect to the remote gateway and save the modified order item) are matched.
