
# coupon
## allowed

Number of coupon codes a customer is allowed to enter

```
controller/frontend/basket/coupon/allowed = 1
```

* Default: `1`
* Type: integer - Positive number of coupon codes including zero
* Since: 2017.08

This configuration option enables shop owners to limit the number of coupon
codes that can be added by a customer to his current basket. By default, only
one coupon code is allowed per order.

Coupon codes are valid until a payed order is placed by the customer. The
"count" of the codes is decreased afterwards. If codes are not personalized
the codes can be reused in the next order until their "count" reaches zero.


# decorators
## excludes

Excludes decorators added by the "common" option from the basket frontend controllers

```
controller/frontend/basket/decorators/excludes = Array
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
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/frontend/common/decorators/default" before they are wrapped
around the frontend controller.

```
 controller/frontend/basket/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Frontend\Common\Decorator\*") added via
"controller/frontend/common/decorators/default" for the basket frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/basket/decorators/global
* controller/frontend/basket/decorators/local

## global

Adds a list of globally available decorators only to the basket frontend controllers

```
controller/frontend/basket/decorators/global = Array
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
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Frontend\Common\Decorator\*") around the frontend controller.

```
 controller/frontend/basket/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Frontend\Common\Decorator\Decorator1" only to the frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/basket/decorators/excludes
* controller/frontend/basket/decorators/local

## local

Adds a list of local decorators only to the basket frontend controllers

```
controller/frontend/basket/decorators/local = Array
(
    [0] => Category
    [1] => Bundle
    [2] => Select
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Frontend\Basket\Decorator\*") around the frontend controller.

```
 controller/frontend/basket/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Frontend\Basket\Decorator\Decorator2" only to the frontend
controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/basket/decorators/excludes
* controller/frontend/basket/decorators/global

# limit-count

Maximum number of orders within the time frame

```
controller/frontend/basket/limit-count = 0
```

* Default: `5`
* Type: integer - Number of orders allowed within the time frame
* Since: 2017.05

Creating new orders is limited to avoid abuse and mitigate denial of
service attacks. The number of orders created within the time frame
configured by "controller/frontend/basket/limit-seconds" are counted
before a new order of the same user (either logged in or identified
by the IP address) is created. If the number of orders is higher than
the configured value, an error message will be shown to the user
instead of creating a new order.

See also:

* controller/frontend/basket/limit-seconds

# limit-seconds

Order limitation time frame in seconds

```
controller/frontend/basket/limit-seconds = 31536000
```

* Default: `900`
* Type: integer - Number of seconds to check orders within
* Since: 2017.05

Creating new orders is limited to avoid abuse and mitigate denial of
service attacks. Within the configured time frame, only a limited
number of orders can be created. All orders of the current user
(either logged in or identified by the IP address) within the last X
seconds are counted. If the total value is higher then the number
configured in "controller/frontend/basket/limit-count", an error
message will be shown to the user instead of creating a new order.

See also:

* controller/frontend/basket/limit-count

# name

Class name of the used basket frontend controller implementation

```
controller/frontend/basket/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2014.03

Each default frontend controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Frontend\Basket\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Frontend\Basket\Mybasket
```

then you have to set the this configuration option:

```
 controller/jobs/frontend/basket/name = Mybasket
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyBasket"!


# require-variant

A variant of a selection product must be chosen

```
controller/frontend/basket/require-variant = 1
```

* Default: `1`
* Type: boolean - True if a variant must be chosen, false if also the selection product with attributes can be added
* Since: 2018.01

Selection products normally consist of several article variants and
by default exactly one article variant of a selection product can be
put into the basket.

By setting this option to false, the selection product including the
chosen attributes (if any attribute values were selected) can be put
into the basket as well. This makes it possible to get all articles
or a subset of articles (e.g. all of a color) at once.

This option replace the "client/html/basket/require-variant" setting.
