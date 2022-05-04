Decorators are a great way to dynamically extend the functionality of a class. They implement the same interface as the service provider and are wrapped around them like the layers of an onion.

![Decorators](Aimeos-decorators.png)

When calling a method of such a wrapped object, the method of the outermost decorator is called first. Each decorator can decide to do something before or after calling the same method of the next decorator. It can even stop and return immediately without calling the underlaying object.

The picture illustrates an example how decorators can be used. Customers should be able to pay by invoice but only if:

* they are logged in
* it's not their first order
* they live in one of the configured countries

Decorators can be stacked infinitely to add the required functionality to an existing service provider. For documentation of how to configure service providers and their decorators, please have a look at the [user manual](../../manual/service-details.md).

# Basic skeleton

The skeleton for the most basic implementation of a service decorator would be:

```php
namespace \Aimeos\MShop\Service\Provider\Decorator;

class Mydecorator
    extends \Aimeos\MShop\Service\Provider\Decorator\Base
    implements \Aimeos\MShop\Service\Provider\Decorator\Iface
{
}
```

It's only important to extend from the base decorator class and implement the decorator interface. The base class already contains default implementations for all delivery and payment service provider methods.

# Intercept methods

A decorator without methods is totally valid but useless. Thus, you should add one or more methods that intercept the calls to the "onion" object and implement some additional functionality. You can intercept any **public method** that is implemented in a delivery or payment service provider.

```php
public function calcPrice( \Aimeos\MShop\Order\Item\Base\Iface $basket ) : \Aimeos\MShop\Price\Item\Iface
{
    // do something before
    $price = $this->getProvider()->calcPrice( $basket );
    // do something after

    return $price
}
```

The code above intercepts the *calcPrice()* method for example. It receives the same parameters as the service provider and must return a value if this is documented in the interface describing the method. The underlying object is available via `$this->getProvider()` and it can be used to call any method of this object. Normally it's the same method as the implemented one but it can be another one too.

For examples of decorators and their implementations, you should have a look at the [available decorators](https://github.com/aimeos/aimeos-core/tree/master/src/MShop/Service/Provider/Decorator) in the Aimeos core.
