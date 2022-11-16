
# decorators
## excludes

Excludes decorators added by the "common" option from the admin log controllers

```
controller/jobs/admin/log/decorators/excludes =
```

* Default:
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
 controller/jobs/admin/log/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/admin/log/decorators/global
* controller/jobs/admin/log/decorators/local

## global

Adds a list of globally available decorators only to the admin log controllers

```
controller/jobs/admin/log/decorators/global =
```

* Default:
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/admin/log/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/admin/log/decorators/excludes
* controller/jobs/admin/log/decorators/local

## local

Adds a list of local decorators only to the admin log controllers

```
controller/jobs/admin/log/decorators/local =
```

* Default:
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Admin\Log\Decorator\*") around this job controller.

```
 controller/jobs/admin/log/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Admin\Log\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/admin/log/decorators/excludes
* controller/jobs/admin/log/decorators/global

# limit-days

Only remove log entries that were created berore the configured number of days

```
controller/jobs/admin/log/limit-days = 0
```

* Default: 30
* Type: integer - Number of days
* Since: 2014.09

This option specifies the number of days log entries will be kept in
the database. Afterwards, they will be removed and archived.

See also:

* controller/jobs/admin/log/path

# name

Class name of the used admin log scheduler controller implementation

```
controller/jobs/admin/log/name =
```

* Default:
* Type: string - Last part of the class name
* Since: 2014.09

Each default log controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Admin\Log\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Admin\Log\Mylog
```

then you have to set the this configuration option:

```
 controller/jobs/admin/log/name = Mylog
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyLog"!


# path

Path to a writable directory where the log archive files should be stored

```
controller/jobs/admin/log/path = logs
```

* Default: logs
* Type: string - Relative file system path in the fs-admin filesystem
* Since: 2014.09

During normal operation, a lot of data can be logged, not only for
errors that have occured. By default, these data is written into the
log database and its size will grow if old log entries are not
removed. There's a job controller available that can delete old log
entries and save the old log entries to the given relative path.

See also:

* controller/jobs/admin/log/limit-days