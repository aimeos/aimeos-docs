
# delivery
## decorators/excludes

Excludes decorators added by the "common" option from the order email delivery controllers

```
controller/jobs/order/email/delivery/decorators/excludes = Array
(
)
```

* Default: Array
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
 controller/jobs/order/email/delivery/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/delivery/decorators/global
* controller/jobs/order/email/delivery/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order email delivery controllers

```
controller/jobs/order/email/delivery/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/email/delivery/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/delivery/decorators/excludes
* controller/jobs/order/email/delivery/decorators/local

## decorators/local

Adds a list of local decorators only to the order email delivery controllers

```
controller/jobs/order/email/delivery/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Email\Delivery\Decorator\*") around this job controller.

```
 controller/jobs/order/email/delivery/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Email\Delivery\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/delivery/decorators/excludes
* controller/jobs/order/email/delivery/decorators/global

## limit-days

Only send delivery e-mails of orders that were created in the past within the configured number of days

```
controller/jobs/order/email/delivery/limit-days = 90
```

* Default: 90
* Type: integer - Number of days
* Since: 2014.03

The delivery e-mails are normally send immediately after the delivery
status has changed. This option prevents e-mails for old order from
being send in case anything went wrong or an update failed to avoid
confusion of customers.

See also:

* controller/jobs/order/email/delivery/status
* controller/jobs/order/email/payment/limit-days
* controller/jobs/service/delivery/process/limit-days

## name

Class name of the used order email delivery scheduler controller implementation

```
controller/jobs/order/email/delivery/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Email\Delivery\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Email\Delivery\Mydelivery
```

then you have to set the this configuration option:

```
 controller/jobs/order/email/delivery/name = Mydelivery
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyDelivery"!


## status

Only send order delivery notification e-mails for these delivery status values

```
controller/jobs/order/email/delivery/status = Array
(
    [0] => 2
    [1] => 3
    [2] => 6
    [3] => 7
)
```

* Default: Array
* Type: integer - Delivery status constant
* Since: 2014.03

Notification e-mail about delivery status changes can be sent for these
status values:
* 0: deleted
* 1: pending
* 2: progress
* 3: dispatched
* 4: delivered
* 5: lost
* 6: refused
* 7: returned

User-defined status values are possible but should be in the private
block of values between 30000 and 32767.

See also:

* controller/jobs/order/email/payment/status
* controller/jobs/order/email/delivery/limit-days

# payment
## decorators/excludes

Excludes decorators added by the "common" option from the order email payment controllers

```
controller/jobs/order/email/payment/decorators/excludes = Array
(
)
```

* Default: Array
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
 controller/jobs/order/email/payment/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/payment/decorators/global
* controller/jobs/order/email/payment/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order email payment controllers

```
controller/jobs/order/email/payment/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/email/payment/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/payment/decorators/excludes
* controller/jobs/order/email/payment/decorators/local

## decorators/local

Adds a list of local decorators only to the order email payment controllers

```
controller/jobs/order/email/payment/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Email\Payment\Decorator\*") around this job controller.

```
 controller/jobs/order/email/payment/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Email\Payment\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/payment/decorators/excludes
* controller/jobs/order/email/payment/decorators/global

## limit-days

Only send payment e-mails of orders that were created in the past within the configured number of days

```
controller/jobs/order/email/payment/limit-days = 30
```

* Default: 30
* Type: integer - Number of days
* Since: 2014.03

The payment e-mails are normally send immediately after the payment
status has changed. This option prevents e-mails for old order from
being send in case anything went wrong or an update failed to avoid
confusion of customers.

See also:

* controller/jobs/order/email/delivery/limit-days
* controller/jobs/service/delivery/process/limit-days

## name

Class name of the used order email payment scheduler controller implementation

```
controller/jobs/order/email/payment/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Email\Payment\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Email\Payment\Mypayment
```

then you have to set the this configuration option:

```
 controller/jobs/order/email/payment/name = Mypayment
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyPayment"!


## status

Only send order payment notification e-mails for these payment status values

```
controller/jobs/order/email/payment/status = Array
(
    [0] => 3
    [1] => 4
    [2] => 5
    [3] => 6
)
```

* Default: Array
* Type: integer - Payment status constant
* Since: 2014.03

Notification e-mail about payment status changes can be sent for these
status values:
* 0: deleted
* 1: canceled
* 2: refused
* 3: refund
* 4: pending
* 5: authorized
* 6: received

User-defined status values are possible but should be in the private
block of values between 30000 and 32767.

See also:

* controller/jobs/order/email/delivery/status
* controller/jobs/order/email/payment/limit-days

# voucher
## decorators/excludes

Excludes decorators added by the "common" option from the order email voucher controllers

```
controller/jobs/order/email/voucher/decorators/excludes = Array
(
)
```

* Default: Array
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
 controller/jobs/order/email/voucher/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/voucher/decorators/global
* controller/jobs/order/email/voucher/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order email voucher controllers

```
controller/jobs/order/email/voucher/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/email/voucher/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/voucher/decorators/excludes
* controller/jobs/order/email/voucher/decorators/local

## decorators/local

Adds a list of local decorators only to the order email voucher controllers

```
controller/jobs/order/email/voucher/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Email\Voucher\Decorator\*") around this job controller.

```
 controller/jobs/order/email/voucher/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Email\Voucher\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/voucher/decorators/excludes
* controller/jobs/order/email/voucher/decorators/global

## limit-days

Only send voucher e-mails of orders that were created in the past within the configured number of days

```
controller/jobs/order/email/voucher/limit-days = 30
```

* Default: 30
* Type: integer - Number of days
* Since: 2018.07

The voucher e-mails are normally send immediately after the voucher
has been ordered. This option prevents e-mails for old orders from
being send in case anything went wrong or an update failed to avoid
confusion of customers.

See also:

* controller/jobs/order/email/voucher/status

## name

Class name of the used order email voucher scheduler controller implementation

```
controller/jobs/order/email/voucher/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Email\Voucher\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Email\Voucher\Myvoucher
```

then you have to set the this configuration option:

```
 controller/jobs/order/email/voucher/name = Myvoucher
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyVoucher"!


## status

Only send e-mails containing voucher for these payment status values

```
controller/jobs/order/email/voucher/status = Array
(
    [0] => 5
    [1] => 6
)
```

* Default: Array
* Type: integer - Payment status constant
* Since: 2018.07

E-mail containing vouchers can be sent for these payment status values:
* 0: deleted
* 1: canceled
* 2: refused
* 3: refund
* 4: pending
* 5: authorized
* 6: received

See also:

* controller/jobs/order/email/voucher/limit-days