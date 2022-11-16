
# decorators
## excludes

Excludes decorators added by the "common" option from the order frontend controllers

```
controller/frontend/order/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/frontend/common/decorators/default" before they are wrapped
around the frontend controller.

```
 controller/frontend/order/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Frontend\Common\Decorator\*") added via
"controller/frontend/common/decorators/default" for the order frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/order/decorators/global
* controller/frontend/order/decorators/local

## global

Adds a list of globally available decorators only to the order frontend controllers

```
controller/frontend/order/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Frontend\Common\Decorator\*") around the frontend controller.

```
 controller/frontend/order/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Frontend\Common\Decorator\Decorator1" only to the frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/order/decorators/excludes
* controller/frontend/order/decorators/local

## local

Adds a list of local decorators only to the order frontend controllers

```
controller/frontend/order/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Frontend\Order\Decorator\*") around the frontend controller.

```
 controller/frontend/order/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Frontend\Catalog\Decorator\Decorator2" only to the frontend
controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/order/decorators/excludes
* controller/frontend/order/decorators/global

# limit-count

Maximum number of invoices within the time frame

```
controller/frontend/order/limit-count = 1
```

* Default: 3
* Type: integer - Number of orders allowed within the time frame
* Since: 2020.10

Creating new invoices is limited to avoid abuse and mitigate denial of
service attacks. The number of invoices created within the time frame
configured by "controller/frontend/invoices/limit-seconds" are counted
before a new invoice of the same user (either logged in or identified
by the IP address) is created. If the number of invoices is higher than
the configured value, an error message will be shown to the user
instead of creating a new invoice.

See also:

* controller/frontend/order/limit-seconds
* controller/frontend/basket/limit-count
* controller/frontend/basket/limit-seconds

# limit-seconds

Invoice limitation time frame in seconds

```
controller/frontend/order/limit-seconds = 31536000
```

* Default: 900
* Type: integer - Number of seconds to check order items within
* Since: 2017.05

Creating new invoices is limited to avoid abuse and mitigate denial of
service attacks. Within the configured time frame, only one invoice
item can be created per order base item. All invoices for the order
base item within the last X seconds are counted.  If there's already
one available, an error message will be shown to the user instead of
creating the new order item.

See also:

* controller/frontend/order/limit-count
* controller/frontend/basket/limit-count
* controller/frontend/basket/limit-seconds

# name

Class name of the used order frontend controller implementation

```
controller/frontend/order/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2014.03

Each default frontend controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Frontend\Order\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Frontend\Order\Myorder
```

then you have to set the this configuration option:

```
 controller/frontend/order/name = Myorder
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyOrder"!
