
# account
## decorators/excludes

Excludes decorators added by the "common" option from the customer email account controllers

```
controller/jobs/customer/email/account/decorators/excludes = Array
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
* Since: 2016.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/customer/email/account/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/email/account/decorators/global
* controller/jobs/customer/email/account/decorators/local

## decorators/global

Adds a list of globally available decorators only to the customer email account controllers

```
controller/jobs/customer/email/account/decorators/global = Array
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
* Since: 2016.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/customer/email/account/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/email/account/decorators/excludes
* controller/jobs/customer/email/account/decorators/local

## decorators/local

Adds a list of local decorators only to the customer email account controllers

```
controller/jobs/customer/email/account/decorators/local = Array
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
* Since: 2016.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Customer\Email\Account\Decorator\*") around this job controller.

```
 controller/jobs/customer/email/account/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Customer\Email\Account\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/email/account/decorators/excludes
* controller/jobs/customer/email/account/decorators/global

## name

Class name of the used product notification e-mail scheduler controller implementation

```
controller/jobs/customer/email/account/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2016.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Customer\Email\Account\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Customer\Email\Account\Myaccount
```

then you have to set the this configuration option:

```
 controller/jobs/customer/email/account/name = Myaccount
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAccount"!


## template-html

Relative path to the template for the HTML part of the account emails.

```
controller/jobs/customer/email/account/template-html = customer/email/account/html
```

* Default: `customer/email/account/html`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/customer/email/account/template-text

## template-text

Relative path to the template for the text part of the account emails.

```
controller/jobs/customer/email/account/template-text = customer/email/account/text
```

* Default: `customer/email/account/text`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/customer/email/account/template-html

# watch
## decorators/excludes

Excludes decorators added by the "common" option from the customer email watch controllers

```
controller/jobs/customer/email/watch/decorators/excludes = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/customer/email/watch/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/email/watch/decorators/global
* controller/jobs/customer/email/watch/decorators/local

## decorators/global

Adds a list of globally available decorators only to the customer email watch controllers

```
controller/jobs/customer/email/watch/decorators/global = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/customer/email/watch/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/email/watch/decorators/excludes
* controller/jobs/customer/email/watch/decorators/local

## decorators/local

Adds a list of local decorators only to the customer email watch controllers

```
controller/jobs/customer/email/watch/decorators/local = Array
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
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Customer\Email\Watch\Decorator\*") around this job controller.

```
 controller/jobs/customer/email/watch/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Customer\Email\Watch\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/email/watch/decorators/excludes
* controller/jobs/customer/email/watch/decorators/global

## name

Class name of the used product notification e-mail scheduler controller implementation

```
controller/jobs/customer/email/watch/name = Standard
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
 \Aimeos\Controller\Jobs\Customer\Email\Watch\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Customer\Email\Watch\Mywatch
```

then you have to set the this configuration option:

```
 controller/jobs/customer/email/watch/name = Mywatch
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyWatch"!


## template-html

Relative path to the template for the HTML part of the watch emails.

```
controller/jobs/customer/email/watch/template-html = customer/email/watch/html
```

* Default: `customer/email/watch/html`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/customer/email/watch/template-text

## template-text

Relative path to the template for the text part of the watch emails.

```
controller/jobs/customer/email/watch/template-text = customer/email/watch/text
```

* Default: `customer/email/watch/text`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/customer/email/watch/template-html