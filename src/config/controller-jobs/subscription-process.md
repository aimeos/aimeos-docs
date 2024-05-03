
# batch-max

Maximum number of subscriptions processed at once by the subscription process job

```
controller/jobs/subscription/process/batch-max = 100
```

* Default: `100`
* Type: integer - Number of subscriptions
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04

This setting configures the maximum number of subscriptions including
orders that will be processed at once. Bigger batches an improve the
performance but requires more memory.

See also:

* controller/jobs/subscription/process/domains
* controller/jobs/subscription/process/names
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status
* controller/jobs/subscription/process/domains
* controller/jobs/subscription/process/names
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status
* controller/jobs/subscription/process/domains
* controller/jobs/subscription/process/names
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status

# begin
## decorators/excludes

Excludes decorators added by the "common" option from the subscription process CSV job controller

```
controller/jobs/subscription/process/begin/decorators/excludes = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/subscription/process/begin/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/begin/decorators/global
* controller/jobs/subscription/process/begin/decorators/local

## decorators/global

Adds a list of globally available decorators only to the subscription process CSV job controller

```
controller/jobs/subscription/process/begin/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/subscription/process/begin/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/begin/decorators/excludes
* controller/jobs/subscription/process/begin/decorators/local

## decorators/local

Adds a list of local decorators only to the subscription process CSV job controller

```
controller/jobs/subscription/process/begin/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Subscription\Process\Begin\Decorator\*") around the job
controller.

```
 controller/jobs/subscription/process/begin/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Subscription\Process\Begin\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/begin/decorators/excludes
* controller/jobs/subscription/process/begin/decorators/global

## name

Class name of the used subscription suggestions scheduler controller implementation

```
controller/jobs/subscription/process/begin/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2018.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Subscription\Process\Begin\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Subscription\Process\Begin\Mybegin
```

then you have to set the this configuration option:

```
 controller/jobs/subscription/process/begin/name = Mybegin
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyBegin"!


# domains

Associated items that should be available too in the subscription

```
controller/jobs/subscription/process/domains = Array
(
    [0] => order
    [1] => order/address
    [2] => order/coupon
    [3] => order/product
    [4] => order/service
)
```

* Default: 
```
Array
(
    [0] => order
    [1] => order/address
    [2] => order/coupon
    [3] => order/product
    [4] => order/service
)
```
* Type: array - Referenced domain names
* Since: 2022.04
* Since: 2022.04
* Since: 2022.04

Orders consist of address, coupons, products and services. They can be
fetched together with the subscription items and passed to the processor.
Available domains for those items are:

- order
- order/address
- order/coupon
- order/product
- order/service

See also:

* controller/jobs/subscription/process/processors
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status
* controller/jobs/subscription/process/processors
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status
* controller/jobs/subscription/process/processors
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status

# end
## decorators/excludes

Excludes decorators added by the "common" option from the subscription process CSV job controller

```
controller/jobs/subscription/process/end/decorators/excludes = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/subscription/process/end/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/end/decorators/global
* controller/jobs/subscription/process/end/decorators/local

## decorators/global

Adds a list of globally available decorators only to the subscription process CSV job controller

```
controller/jobs/subscription/process/end/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/subscription/process/end/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/end/decorators/excludes
* controller/jobs/subscription/process/end/decorators/local

## decorators/local

Adds a list of local decorators only to the subscription process CSV job controller

```
controller/jobs/subscription/process/end/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Subscription\Process\End\Decorator\*") around the job
controller.

```
 controller/jobs/subscription/process/end/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Subscription\Process\End\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/end/decorators/excludes
* controller/jobs/subscription/process/end/decorators/global

## name

Class name of the used subscription suggestions scheduler controller implementation

```
controller/jobs/subscription/process/end/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2018.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Subscription\Process\End\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Subscription\Process\End\Myend
```

then you have to set the this configuration option:

```
 controller/jobs/subscription/process/end/name = Myend
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyEnd"!


# payment-days

Number of days to wait for the payment until subscription is removed

```
controller/jobs/subscription/process/payment-days = 
```

* Type: float - Number of days
* Since: 2018.07

Subscriptions wait for the confiugrable number of days until the payment
status changes to a valid payment (by default: "authorized" and "received").
If the payment arrives within this time frame, the subscription is activated.
Otherwise, the subscription is removed from the list of subscriptions that
will be checked for activation.

See also:

* controller/jobs/subscription/process/processors
* controller/jobs/subscription/process/payment-status

# payment-ends

Subscriptions ends if payment couldn't be captured

```
controller/jobs/subscription/process/payment-ends = 
```

* Type: bool - TRUE if payment failures ends the subscriptions, FALSE if not
* Since: 2019.10

By default, a subscription ends automatically if the next payment couldn't
be captured. When setting this configuration to FALSE, the subscription job
controller will try to capture the payment at the next run again until the
subscription is deactivated manually.

See also:

* controller/jobs/subscription/process/processors
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status

# payment-status

Minimum payment status that will activate the subscription

```
controller/jobs/subscription/process/payment-status = 5
```

* Default: `5`
* Type: integer - Payment status constant
* Since: 2018.07

Subscriptions will be activated if the payment status of the order is
at least the configured payment constant. The default payment status
is "authorized" so orders with a payment status of "authorized" (5) and
"received" (6) will cause the subscription to be activated. Lower
payment status values, e.g. "pending" (4) won't activate the subscription.

See also:

* controller/jobs/subscription/process/begin/domains
* controller/jobs/subscription/process/begin/max
* controller/jobs/subscription/process/begin/names
* controller/jobs/subscription/process/payment-days

# processor
## cgroup/groupids

List of group IDs that should be added to the customer account

```
controller/jobs/subscription/process/processor/cgroup/groupids = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of customer group IDs
* Since: 2018.04

After customers bought a subscription, the list of group IDs will be
added to their accounts. When the subscription period ends, they will
be removed from the customer accounts again.


## cgroup/name

Name of the customer group processor implementation

```
controller/jobs/subscription/process/processor/cgroup/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2018.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Subscription\Process\Processor\Cgroup\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


# processors

List of processor names that should be executed for subscriptions

```
controller/jobs/subscription/process/processors = Array
(
    [0] => cgroup
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of processor names
* Since: 2018.04
* Since: 2018.04
* Since: 2018.04

For each subscription a number of processors for different tasks can be executed.
They can for example add a group to the customers' account during the customer
has an active subscribtion.

See also:

* controller/jobs/subscription/process/domains
* controller/jobs/subscription/process/max
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status
* controller/jobs/subscription/process/domains
* controller/jobs/subscription/process/max
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status
* controller/jobs/subscription/process/domains
* controller/jobs/subscription/process/max
* controller/jobs/subscription/process/payment-days
* controller/jobs/subscription/process/payment-status

# renew
## decorators/excludes

Excludes decorators added by the "common" option from the subscription process CSV job controller

```
controller/jobs/subscription/process/renew/decorators/excludes = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extrenew the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/subscription/process/renew/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/renew/decorators/global
* controller/jobs/subscription/process/renew/decorators/local

## decorators/global

Adds a list of globally available decorators only to the subscription process CSV job controller

```
controller/jobs/subscription/process/renew/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extrenew the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/subscription/process/renew/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/renew/decorators/excludes
* controller/jobs/subscription/process/renew/decorators/local

## decorators/local

Adds a list of local decorators only to the subscription process CSV job controller

```
controller/jobs/subscription/process/renew/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2018.04

Decorators extrenew the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Subscription\Process\Renew\Decorator\*") around the job
controller.

```
 controller/jobs/subscription/process/renew/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Subscription\Process\Renew\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/process/renew/decorators/excludes
* controller/jobs/subscription/process/renew/decorators/global

## name

Class name of the used subscription suggestions scheduler controller implementation

```
controller/jobs/subscription/process/renew/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2018.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Subscription\Process\Renew\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Subscription\Process\Renew\Myrenew
```

then you have to set the this configuration option:

```
 controller/jobs/subscription/process/renew/name = Myrenew
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyRenew"!


## use-coupons

Applies the coupons of the previous order also to the new one

```
controller/jobs/subscription/process/renew/use-coupons = 
```

* Default: ``
* Type: boolean - True to reuse coupon codes, false to remove coupons
* Since: 2018.10

Reuse coupon codes added to the order by the customer the first time
again in new subscription orders. If they have any effect depends on
the codes still being active (status, time frame and count) and the
decorators added to the coupon providers in the admin interface.
