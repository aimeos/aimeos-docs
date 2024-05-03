
# unfinished
## decorators/excludes

Excludes decorators added by the "common" option from the order cleanup unfinished controllers

```
controller/jobs/order/cleanup/unfinished/decorators/excludes = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/cleanup/unfinished/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/cleanup/unfinished/decorators/global
* controller/jobs/order/cleanup/unfinished/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order cleanup unfinished controllers

```
controller/jobs/order/cleanup/unfinished/decorators/global = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/cleanup/unfinished/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/cleanup/unfinished/decorators/excludes
* controller/jobs/order/cleanup/unfinished/decorators/local

## decorators/local

Adds a list of local decorators only to the order cleanup unfinished controllers

```
controller/jobs/order/cleanup/unfinished/decorators/local = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Cleanup\Unfinished\Decorator\*") around this job controller.

```
 controller/jobs/order/cleanup/unfinished/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Cleanup\Unfinished\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/cleanup/unfinished/decorators/excludes
* controller/jobs/order/cleanup/unfinished/decorators/global

## keep-hours

Release the ordered products after the configured time if no payment was confirmed

```
controller/jobs/order/cleanup/unfinished/keep-hours = 24
```

* Default: `24`
* Type: integer - Number of hours
* Since: 2014.07

After a customer creates an order and before he is redirected to the
payment provider (if necessary), the ordered products, coupon codes,
etc. are blocked for that customer. Normally, they should be released
a certain amount of time if no payment confirmation arrives so
customers can order the products and use the coupon codes again.

The configured number of hours should be high enough to avoid releasing
products and coupon codes in case of temporary technical problems!

The unfinished orders are deleted afterwards to keep the database clean.


## name

Class name of the used order cleanup unfinished scheduler controller implementation

```
controller/jobs/order/cleanup/unfinished/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2014.03

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Cleanup\Unfinished\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Cleanup\Unfinished\Myunfinished
```

then you have to set the this configuration option:

```
 controller/jobs/order/cleanup/unfinished/name = Myunfinished
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyUnfinished"!


# unpaid
## decorators/excludes

Excludes decorators added by the "common" option from the order cleanup unpaid controllers

```
controller/jobs/order/cleanup/unpaid/decorators/excludes = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/cleanup/unpaid/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/cleanup/unpaid/decorators/global
* controller/jobs/order/cleanup/unpaid/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order cleanup unpaid controllers

```
controller/jobs/order/cleanup/unpaid/decorators/global = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/cleanup/unpaid/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/cleanup/unpaid/decorators/excludes
* controller/jobs/order/cleanup/unpaid/decorators/local

## decorators/local

Adds a list of local decorators only to the order cleanup unpaid controllers

```
controller/jobs/order/cleanup/unpaid/decorators/local = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Cleanup\Unpaid\Decorator\*") around this job controller.

```
 controller/jobs/order/cleanup/unpaid/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Cleanup\Unpaid\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/cleanup/unpaid/decorators/excludes
* controller/jobs/order/cleanup/unpaid/decorators/global

## keep-days

Removes all orders from the database that are unpaid

```
controller/jobs/order/cleanup/unpaid/keep-days = 3
```

* Default: `3`
* Type: integer - Number of days
* Since: 2014.07

Orders with a payment status of deleted, canceled or refused are only
necessary for the records for a certain amount of time. Afterwards,
they can be deleted from the database most of the time.

The number of days should be high enough to ensure that you keep the
orders as long as your customers will be asking what happend to their
orders.


## name

Class name of the used order cleanup unpaid scheduler controller implementation

```
controller/jobs/order/cleanup/unpaid/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2014.07

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Cleanup\Unpaid\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Cleanup\Unpaid\Myunpaid
```

then you have to set the this configuration option:

```
 controller/jobs/order/cleanup/unpaid/name = Myunpaid
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyUnpaid"!
