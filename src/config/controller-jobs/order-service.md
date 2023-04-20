
# async
## decorators/excludes

Excludes decorators added by the "common" option from the order service async controllers

```
controller/jobs/order/service/async/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/service/async/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/async/decorators/global
* controller/jobs/order/service/async/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order service async controllers

```
controller/jobs/order/service/async/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/service/async/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/async/decorators/excludes
* controller/jobs/order/service/async/decorators/local

## decorators/local

Adds a list of local decorators only to the order service async controllers

```
controller/jobs/order/service/async/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Service\Async\Decorator\*") around this job controller.

```
 controller/jobs/order/service/async/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Service\Async\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/async/decorators/excludes
* controller/jobs/order/service/async/decorators/global

## name

Class name of the used order service async scheduler controller implementation

```
controller/jobs/order/service/async/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2014.07

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Service\Async\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Service\Async\Myasync
```

then you have to set the this configuration option:

```
 controller/jobs/order/service/async/name = Myasync
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAsync"!


# delivery
## batch-max

Maximum number of orders processed at once by the delivery service provider

```
controller/jobs/order/service/delivery/batch-max = 100
```

* Default: 100
* Type: integer - Number of orders
* Since: 2018.07
* Since: 2018.07

Orders are sent in batches if the delivery service provider supports it.
This setting configures the maximum orders that will be handed over to
the delivery service provider at once. Bigger batches an improve the
performance but requires more memory.

See also:

* controller/jobs/order/service/delivery/domains
* controller/jobs/order/service/delivery/limit-days
* controller/jobs/order/service/delivery/domains
* controller/jobs/order/service/delivery/limit-days

## decorators/excludes

Excludes decorators added by the "common" option from the order service delivery controllers

```
controller/jobs/order/service/delivery/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/service/delivery/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/delivery/decorators/global
* controller/jobs/order/service/delivery/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order service delivery controllers

```
controller/jobs/order/service/delivery/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/service/delivery/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/delivery/decorators/excludes
* controller/jobs/order/service/delivery/decorators/local

## decorators/local

Adds a list of local decorators only to the order service delivery controllers

```
controller/jobs/order/service/delivery/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Service\Delivery\Decorator\*") around this job controller.

```
 controller/jobs/order/service/delivery/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Service\Delivery\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/delivery/decorators/excludes
* controller/jobs/order/service/delivery/decorators/global

## domains

Associated items that should be available too in the order

```
controller/jobs/order/service/delivery/domains = Array
(
    [order/address] => order/address
    [order/coupon] => order/coupon
    [order/product] => order/product
    [order/service] => order/service
)
```

* Default: Array
(
    [order/address] => order/address
    [order/coupon] => order/coupon
    [order/product] => order/product
    [order/service] => order/service
)

* Type: array - Referenced domain names
* Since: 2022.04

Orders consist of address, coupons, products and services. They can be
fetched together with the order items and passed to the delivery service
providers. Available domains for those items are:

- order/address
- order/coupon
- order/product
- order/service

See also:

* controller/jobs/order/email/delivery/limit-days
* controller/jobs/order/service/delivery/batch-max

## limit-days

Only start the delivery process of orders that were created in the past within the configured number of days

```
controller/jobs/order/service/delivery/limit-days = 90
```

* Default: 90
* Type: integer - Number of days
* Since: 2014.03

The delivery process is normally started immediately after the
notification about a successful payment arrived. This option prevents
orders from being shipped in case anything went wrong or an update
failed and old orders would have been shipped now.

See also:

* controller/jobs/order/service/delivery/batch-max
* controller/jobs/order/service/delivery/domains

## name

Class name of the used order service delivery scheduler controller implementation

```
controller/jobs/order/service/delivery/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2014.03

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Service\Delivery\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Service\Delivery\Mydelivery
```

then you have to set the this configuration option:

```
 controller/jobs/order/service/delivery/name = Mydelivery
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyDelivery"!


# payment
## capture-days

Automatically capture payments after the configured amount of days

```
controller/jobs/order/service/payment/capture-days = 
```

* Default: 
* Type: integer - Number of days
* Since: 2014.07

You can capture authorized payments after a configured amount of days
even if the parcel for the order wasn't dispatched yet. This is useful
for payment methods like credit cards where autorizations are revoked
by the aquirers after some time (usually seven days).


## decorators/excludes

Excludes decorators added by the "common" option from the order service payment controllers

```
controller/jobs/order/service/payment/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/service/payment/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/payment/decorators/global
* controller/jobs/order/service/payment/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order service payment controllers

```
controller/jobs/order/service/payment/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/service/payment/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/payment/decorators/excludes
* controller/jobs/order/service/payment/decorators/local

## decorators/local

Adds a list of local decorators only to the order service payment controllers

```
controller/jobs/order/service/payment/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Service\Payment\Decorator\*") around this job controller.

```
 controller/jobs/order/service/payment/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Service\Payment\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/payment/decorators/excludes
* controller/jobs/order/service/payment/decorators/global

## domains

Associated items that should be available too in the order

```
controller/jobs/order/service/payment/domains = 
```

* Default: 
* Type: array - Referenced domain names
* Since: 2022.04

Orders consist of address, coupons, products and services. They can be
fetched together with the order items and passed to the payment service
providers. Available domains for those items are:

- order/address
- order/coupon
- order/product
- order/service

See also:

* controller/jobs/order/email/payment/limit-days
* controller/jobs/order/service/payment/capture-days

## limit-days

Only start capturing payments of orders that were created in the past within the configured number of days

```
controller/jobs/order/service/payment/limit-days = 90
```

* Default: 90
* Type: integer - Number of days
* Since: 2014.07

Capturing payments is normally done immediately after the delivery
status changed to "dispatched" or "delivered". This option prevents
payments from being captured in case anything went wrong and payments
of old orders would be captured now.


## name

Class name of the used order service payment scheduler controller implementation

```
controller/jobs/order/service/payment/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2014.07

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Service\Payment\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Service\Payment\Mypayment
```

then you have to set the this configuration option:

```
 controller/jobs/order/service/payment/name = Mypayment
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyPayment"!


# transfer
## batch-max

Maximum number of orders processed at once by the payment service provider

```
controller/jobs/order/service/transfer/batch-max = 100
```

* Default: 100
* Type: integer - Number of orders
* Since: 2023.04

Orders are sent in batches if the payment service provider supports it.
This setting configures the maximum orders that will be handed over to
the payment service provider at once. Bigger batches an improve the
performance but requires more memory.

See also:

* controller/jobs/order/service/transfer/domains
* controller/jobs/order/service/transfer/limit-days

## decorators/excludes

Excludes decorators added by the "common" option from the order service transfer controllers

```
controller/jobs/order/service/transfer/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2021.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/service/transfer/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/transfer/decorators/global
* controller/jobs/order/service/transfer/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order service transfer controllers

```
controller/jobs/order/service/transfer/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2021.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/service/transfer/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/transfer/decorators/excludes
* controller/jobs/order/service/transfer/decorators/local

## decorators/local

Adds a list of local decorators only to the order service transfer controllers

```
controller/jobs/order/service/transfer/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2021.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Service\Transfer\Decorator\*") around this job controller.

```
 controller/jobs/order/service/transfer/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Service\Transfer\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/service/transfer/decorators/excludes
* controller/jobs/order/service/transfer/decorators/global

## domains

Associated items that should be available too in the order

```
controller/jobs/order/service/transfer/domains = Array
(
    [order/address] => order/address
    [order/coupon] => order/coupon
    [order/product] => order/product
    [order/service] => order/service
)
```

* Default: Array
(
    [order/address] => order/address
    [order/coupon] => order/coupon
    [order/product] => order/product
    [order/service] => order/service
)

* Type: array - Referenced domain names
* Since: 2022.04

Orders consist of address, coupons, products and services. They can be
fetched together with the order items and passed to the payment service
providers. Available domains for those items are:

- order/address
- order/coupon
- order/product
- order/service


## name

Class name of the used order service transfer scheduler controller implementation

```
controller/jobs/order/service/transfer/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2021.10

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Service\Transfer\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Service\Transfer\Mytransfer
```

then you have to set the this configuration option:

```
 controller/jobs/order/service/transfer/name = Mytransfer
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyTransfer"!


## transfer-days

Automatically transfers payments after the configured amount of days

```
controller/jobs/order/service/transfer/transfer-days = 0
```

* Default: 0
* Type: integer - Number of days
* Since: 2010.10

You can start transferring payments after the configured amount of days.
Before, the money is hold back and not available to vendors.
