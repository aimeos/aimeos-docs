
# decorators

Adds a list of decorators to all coupon provider objects automatcally

```
mshop/coupon/provider/decorators = 
```

* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap decorators
("\Aimeos\MShop\Coupon\Provider\Decorator\*") around the coupon provider.

```
 mshop/coupon/provider/decorators = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Coupon\Provider\Decorator\Decorator1" to all coupon provider
objects.

See also:

* client/html/common/decorators/default
* client/html/account/favorite/decorators/excludes
* client/html/account/favorite/decorators/local

# unfinished-hours

Number of hours unfinished orders count as coupon code redemption

```
mshop/coupon/provider/unfinished-hours = 
```

* Type: int - Number of hours
* Since: 2026.10

Orders are stored with an "unfinished" payment status before the
customer is redirected to the payment provider and the coupon code
counts are only decreased after the payment has been confirmed. To
prevent customers from redeeming the same code in several orders
before confirming the first one, unfinished orders created within
the configured time frame are counted too. The value should match
the time unfinished orders are kept before they are removed.

See also:

* controller/jobs/order/cleanup/unfinished/keep-hours