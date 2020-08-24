
# begin
## decorators/excludes

Excludes decorators added by the "common" option from the subscription process CSV job controller

```
controller/jobs/subscription/process/begin/decorators/excludes = Array
(
)
```

* Default: Array
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

* Default: Array
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

* Default: Array
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

* Default: Standard
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


# end
## decorators/excludes

Excludes decorators added by the "common" option from the subscription process CSV job controller

```
controller/jobs/subscription/process/end/decorators/excludes = Array
(
)
```

* Default: Array
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

* Default: Array
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

* Default: Array
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

* Default: Standard
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


# renew
## decorators/excludes

Excludes decorators added by the "common" option from the subscription process CSV job controller

```
controller/jobs/subscription/process/renew/decorators/excludes = Array
(
)
```

* Default: Array
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

* Default: Array
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

* Default: Array
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

* Default: Standard
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


## standard/use-coupons

Applies the coupons of the previous order also to the new one

```
controller/jobs/subscription/process/renew/standard/use-coupons = 
```

* Default: 
* Type: boolean - True to reuse coupon codes, false to remove coupons
* Since: 2018.10

Reuse coupon codes added to the basket by the customer the first time
again in new subscription orders. If they have any effect depends on
the codes still being active (status, time frame and count) and the
decorators added to the coupon providers in the admin interface.
