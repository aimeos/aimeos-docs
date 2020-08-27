
# decorators
## excludes

Excludes decorators added by the "common" option from the subscription frontend controllers

```
controller/frontend/subscription/decorators/excludes = Array
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
"controller/frontend/common/decorators/default" before they are wrapped
around the frontend controller.

```
 controller/frontend/subscription/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Frontend\Common\Decorator\*") added via
"controller/frontend/common/decorators/default" for the subscription frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/subscription/decorators/global
* controller/frontend/subscription/decorators/local

## global

Adds a list of globally available decorators only to the subscription frontend controllers

```
controller/frontend/subscription/decorators/global = Array
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
("\Aimeos\Controller\Frontend\Common\Decorator\*") around the frontend controller.

```
 controller/frontend/subscription/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Frontend\Common\Decorator\Decorator1" only to the frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/subscription/decorators/excludes
* controller/frontend/subscription/decorators/local

## local

Adds a list of local decorators only to the subscription frontend controllers

```
controller/frontend/subscription/decorators/local = Array
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
("\Aimeos\Controller\Frontend\Subscription\Decorator\*") around the frontend controller.

```
 controller/frontend/subscription/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Frontend\Catalog\Decorator\Decorator2" only to the frontend
controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/subscription/decorators/excludes
* controller/frontend/subscription/decorators/global

# name

Class name of the used subscription frontend controller implementation

```
controller/frontend/subscription/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.04

Each default frontend controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Frontend\Subscription\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Frontend\Subscription\Mysubscription
```

then you have to set the this configuration option:

```
 controller/frontend/subscription/name = Mysubscription
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MySubscription"!
