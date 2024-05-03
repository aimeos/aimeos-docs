
# default

Configures the list of decorators applied to all job controllers

```
controller/jobs/common/decorators/default = Array
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

This option allows you to configure a list of decorator names that should
be wrapped around the original instance of all created controllers:

```
 controller/jobs/common/decorators/default = array( 'decorator1', 'decorator2' )
```

This would wrap the decorators named "decorator1" and "decorator2" around
all controller instances in that order. The decorator classes would be
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" and
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator2".
