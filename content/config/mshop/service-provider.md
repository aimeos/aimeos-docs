
# delivery
## decorators

Adds a list of decorators to all delivery provider objects automatcally

```
mshop/service/provider/delivery/decorators = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap decorators
("\Aimeos\MShop\Service\Provider\Decorator\*") around the delivery provider.

```
 mshop/service/provider/delivery/decorators = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Service\Provider\Decorator\Decorator1" to all delivery provider
objects.

See also:

* mshop/service/provider/payment/decorators

# payment
## decorators

Adds a list of decorators to all payment provider objects automatcally

```
mshop/service/provider/payment/decorators = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap decorators
("\Aimeos\MShop\Service\Provider\Decorator\*") around the payment provider.

```
 mshop/service/provider/payment/decorators = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Service\Provider\Decorator\Decorator1" to all payment provider
objects.

See also:

* mshop/service/provider/delivery/decorators