
# default

Configures the list of decorators applied to all html clients

```
client/html/common/decorators/default = Array
(
    [0] => Context
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to configure a list of decorator names that should
be wrapped around the original instance of all created clients:

```
 client/html/common/decorators/default = array( 'decorator1', 'decorator2' )
```

This would wrap the decorators named "decorator1" and "decorator2" around
all client instances in that order. The decorator classes would be
"\Aimeos\Client\Html\Common\Decorator\Decorator1" and
"\Aimeos\Client\Html\Common\Decorator\Decorator2".
