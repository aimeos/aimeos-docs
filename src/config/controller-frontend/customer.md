
# decorators
## excludes

Excludes decorators added by the "common" option from the customer frontend controllers

```
controller/frontend/customer/decorators/excludes =
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
 controller/frontend/customer/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Frontend\Common\Decorator\*") added via
"controller/frontend/common/decorators/default" for the customer frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/customer/decorators/global
* controller/frontend/customer/decorators/local

## global

Adds a list of globally available decorators only to the customer frontend controllers

```
controller/frontend/customer/decorators/global =
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
 controller/frontend/customer/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Frontend\Common\Decorator\Decorator1" only to the frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/customer/decorators/excludes
* controller/frontend/customer/decorators/local

## local

Adds a list of local decorators only to the customer frontend controllers

```
controller/frontend/customer/decorators/local =
```

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Frontend\Customer\Decorator\*") around the frontend controller.

```
 controller/frontend/customer/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Frontend\Customer\Decorator\Decorator2" only to the frontend
controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/customer/decorators/excludes
* controller/frontend/customer/decorators/global

# groupids

List of groups new customers should be assigned to

```
controller/frontend/groupids = Array
(
)
```

* Default: Array
(
)

* Type: array - List of group IDs
* Since: 2017.07

Newly created customers will be assigned automatically to the groups
given by their IDs. This is especially useful if those groups limit
functionality for those users.


# limit-count

Maximum number of customers within the time frame

```
controller/frontend/customer/limit-count = 3
```

* Default: 3
* Type: integer - Number of customer accounts allowed within the time frame
* Since: 2017.07

Creating new customers is limited to avoid abuse and mitigate denial of
service attacks. The number of customer accountss created within the
time frame configured by "controller/frontend/customer/limit-seconds"
are counted before a new customer account (identified by the IP address)
is created. If the number of accounts is higher than the configured value,
an error message will be shown to the user instead of creating a new account.

See also:

* controller/frontend/customer/limit-seconds

# limit-seconds

Customer account limitation time frame in seconds

```
controller/frontend/customer/limit-seconds = 14400
```

* Default: 14400
* Type: integer - Number of seconds to check customer accounts within
* Since: 2017.07

Creating new customer accounts is limited to avoid abuse and mitigate
denial of service attacks. Within the configured time frame, only a
limited number of customer accounts can be created. All accounts from
the same source (identified by the IP address) within the last X
seconds are counted. If the total value is higher then the number
configured in "controller/frontend/customer/limit-count", an error
message will be shown to the user instead of creating a new account.

See also:

* controller/frontend/customer/limit-count

# name

Class name of the used customer frontend controller implementation

```
controller/frontend/customer/name =
```

* Type: string - Last part of the class name
* Since: 2014.03

Each default frontend controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Frontend\Customer\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Frontend\Customer\Mycustomer
```

then you have to set the this configuration option:

```
 controller/frontend/customer/name = Mycustomer
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCustomer"!
