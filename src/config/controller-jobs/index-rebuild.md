
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog index rebuild controllers

```
controller/jobs/index/rebuild/decorators/excludes = Array
(
)
```

* Default: `Array
(
)
`
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
 controller/jobs/index/rebuild/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/index/rebuild/decorators/global
* controller/jobs/index/rebuild/decorators/local

## global

Adds a list of globally available decorators only to the catalog index rebuild controllers

```
controller/jobs/index/rebuild/decorators/global = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/index/rebuild/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/index/rebuild/decorators/excludes
* controller/jobs/index/rebuild/decorators/local

## local

Adds a list of local decorators only to the catalog index rebuild controllers

```
controller/jobs/index/rebuild/decorators/local = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Index\Rebuild\Decorator\*") around this job controller.

```
 controller/jobs/index/rebuild/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Index\Rebuild\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/index/rebuild/decorators/excludes
* controller/jobs/index/rebuild/decorators/global

# name

Class name of the used catalog index rebuild scheduler controller implementation

```
controller/jobs/index/rebuild/name = Standard
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
 \Aimeos\Controller\Jobs\Index\Rebuild\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Index\Rebuild\Myrebuild
```

then you have to set the this configuration option:

```
 controller/index/rebuild/name = Myrebuild
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyRebuild"!
