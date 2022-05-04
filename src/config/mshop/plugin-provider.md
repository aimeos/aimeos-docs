
# order
## complete/disable

Disables the basket limits check

```
mshop/plugin/provider/order/complete/disable = 
```

* Default: 
* Type: bool - True to disable the check, false to keep it enabled
* Since: 2014.03

If the BasketLimits plug-in is enabled, it enforces the configured
limits before customers or anyone on behalf of them can continue the
checkout process.

This option enables e.g. call center agents to place orders which
doesn't satisfy all requirements. It may be useful if you want to
allow them to send free or replacements for lost or damaged products.


## decorators

Adds a list of decorators to all order plugin provider objects automatcally

```
mshop/plugin/provider/order/decorators = Array
(
    [0] => Log
    [1] => Singleton
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap decorators
("\Aimeos\MShop\Plugin\Provider\Decorator\*") around the order provider.

```
 mshop/plugin/provider/order/decorators = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Plugin\Provider\Decorator\Decorator1" to all order provider
objects.

See also:

* mshop/plugin/provider/order/decorators