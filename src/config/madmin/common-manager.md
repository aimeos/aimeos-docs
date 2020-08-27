
# decorators
## default

Configures the list of decorators applied to all admin managers

```
madmin/common/manager/decorators/default = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to configure a list of decorator names that should
be wrapped around the original instances of all created managers:

```
 madmin/common/manager/decorators/default = array( 'decorator1', 'decorator2' )
```

This would wrap the decorators named "decorator1" and "decorator2" around
all controller instances in that order. The decorator classes would be
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" and
"\Aimeos\MShop\Common\Manager\Decorator\Decorator2".
