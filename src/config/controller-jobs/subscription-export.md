
# csv
## decorators/excludes

Excludes decorators added by the "common" option from the subscription export CSV job controller

```
controller/jobs/subscription/export/csv/decorators/excludes = Array
(
)
```

* Default: `Array
(
)
`
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
 controller/jobs/subscription/export/csv/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/export/csv/decorators/global
* controller/jobs/subscription/export/csv/decorators/local

## decorators/global

Adds a list of globally available decorators only to the subscription export CSV job controller

```
controller/jobs/subscription/export/csv/decorators/global = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/subscription/export/csv/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/export/csv/decorators/excludes
* controller/jobs/subscription/export/csv/decorators/local

## decorators/local

Adds a list of local decorators only to the subscription export CSV job controller

```
controller/jobs/subscription/export/csv/decorators/local = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Subscription\Export\Csv\Decorator\*") around the job
controller.

```
 controller/jobs/subscription/export/csv/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Subscription\Export\Csv\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/export/csv/decorators/excludes
* controller/jobs/subscription/export/csv/decorators/global

## max-size

Maximum number of CSV rows to export at once

```
controller/jobs/subscription/export/csv/max-size = 1000
```

* Default: `1000`
* Type: integer - Number of rows
* Since: 2023.04

It's more efficient to read and export more than one row at a time
to speed up the export. Usually, the bigger the chunk that is exported
at once, the less time the exporter will need. The downside is that
the amount of memory required by the export process will increase as
well. Therefore, it's a trade-off between memory consumption and
export speed.


## name

Class name of the used subscription suggestions scheduler controller implementation

```
controller/jobs/subscription/export/csv/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2018.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Subscription\Export\Csv\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Subscription\Export\Csv\Mycsv
```

then you have to set the this configuration option:

```
 controller/jobs/subscription/export/csv/name = Mycsv
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCsv"!


## path

Relativ path to the export file

```
controller/jobs/subscription/export/csv/path = subscription-export_%Y-%m-%d_%H-%i-%s
```

* Default: `subscription-export_%Y-%m-%d_%H-%i-%s`
* Type: string - Relativ path with placeholders
* Since: 2023.04

It's more efficient to read and export more than one row at a time
to speed up the export. Usually, the bigger the chunk that is exported
at once, the less time the exporter will need. The downside is that
the amount of memory required by the export process will increase as
well. Therefore, it's a trade-off between memory consumption and
export speed.


## template

Relative path to the template for generating the CSV subscription export.

```
controller/jobs/subscription/export/csv/template = subscription/export/csv/body
```

* Default: `subscription/export/csv/body`
* Type: string - Relative path to the template
* Since: 2023.04

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.
